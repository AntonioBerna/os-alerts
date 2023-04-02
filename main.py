from dotenv import dotenv_values
import requests
import telebot
import pymongo
import time

class MongoManager:
    def __init__(self, config: dict) -> None:
        self.link = f"mongodb+srv://{config['USERNAME']}:{config['PASSWORD']}@{config['CLUSTER']}.{config['SESSION']}.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.link)

    def get_database_list(self) -> list[str]:
        return self.client.list_database_names()

    def get_collections_list(self) -> list[str]:
        return self.client.telegram.list_collection_names()
    
    def check_and_update(self, html: str) -> bool:
        search = self.client.telegram.html.find_one({"length": {"$exists": True}})
        if search != None and search["length"] != str(len(html)):
            search["length"] = str(len(html))
            self.client.telegram.html.update_one({"_id": search["_id"]}, {"$set": search})
            return True
        return False

class Scraper:
    def __init__(self, config: dict) -> None:
        self.url = config["URL_2023"]
        self.hour = float(config["HOUR"])
        self.manager = MongoManager(config=config)

    def get_data(self) -> bool:
        return self.manager.check_and_update(requests.get(url=self.url).text)

config = dict(dotenv_values(".env"))
bot = telebot.TeleBot(token=config["TOKEN"])

@bot.message_handler(commands=["start"])
def send_start(message):
    bot.send_message(message.chat.id, text=f"Benvenuto {message.chat.username}!")
    scraper = Scraper(config)
    while True:
        if scraper.get_data():
            bot.send_message(message.chat.id, text=f"Nuovi Avvisi Disponibili:\n{config['URL_2023']}")
        time.sleep(float(config["HOUR"]) * 3600)

@bot.message_handler(commands=["alive"])
def send_alive(message):
    bot.send_message(message.chat.id, text="I'm alive!")

if __name__ == "__main__":
    print("Bot running.")
    bot.polling()
    print()

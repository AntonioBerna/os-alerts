from dotenv import dotenv_values
import time

# my libraries
from scraper import Scraper
from telegram import Telegram
from manager import MongoManager

def update_log(e: Exception):
    with open("log.txt", "a") as f:
        f.write(f"{e}\n")

def main(config):
    scraper = Scraper(config=config)
    bot = Telegram(config=config)
    manager = MongoManager(config=config)

    while True:
        if manager.check_and_update(scraper.get_data()):
            bot.send_message(chat_id=config["CHAT_ID"], text=f"<b>Nuovi Avvisi Disponibili:</b>\n{config['URL_2023']}")
        time.sleep(float(config["HOUR"]) * 3600)

if __name__ == "__main__":
    config_mode = False
    if config_mode:
        from dotenv import dotenv_values
        config = dict(dotenv_values(".env"))
    else:
        import json
        config = json.load(open("config.json"))
    
    try:
        print("Bot running.")
        from keep_alive import keep_alive
        keep_alive()
        main(config)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        update_log(e)
        print("\nlog.txt has been updated.")

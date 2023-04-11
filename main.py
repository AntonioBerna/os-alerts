from dotenv import dotenv_values
import argparse
import time

# my libraries
from telegram import Telegram
from scraper import Scraper

def main(config, manager):
    scraper = Scraper(config=config)
    bot = Telegram(config=config)

    while True:
        if manager.check_and_update(scraper.get_data()):
            bot.send_message(chat_id=config["CHAT_ID"], text=f"<b>Nuovi Avvisi Disponibili:</b>\n{config['URL_2023']}")
        time.sleep(float(config["HOUR"]) * 3600)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", dest="env", help="set environment variables with .env file")
    parser.add_argument("--mongo", dest="mongo", help="use mongo database")
    parser.set_defaults(mongo=False)

    args = parser.parse_args()
    # print(args)
    
    if args.env is not None:
        config = dict(dotenv_values(args.env))
    
    if args.mongo:
        from mongo_manager import MongoManager
        manager = MongoManager(config=config)
    else:
        from file_manager import FileManager
        manager = FileManager()
    
    try:
        print("Bot running.")
        main(config, manager)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\n{e}")


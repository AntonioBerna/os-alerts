from dotenv import dotenv_values
from telegram import Telegram
from scraper import Scraper
import threading
import time
import os
import sys

def main(config, manager):
    scraper = Scraper(config=config)
    bot = Telegram(config=config)

    while True:
        if manager.check_and_update(scraper.get_data()):
            bot.send_message(chat_id=config["CHAT_ID"], text=f"<b>Nuovi Avvisi Disponibili:</b>\n{config['URL_2023']}")
        time.sleep(float(config["HOUR"]) * 3600)

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--env", dest="env", help="set environment variables with .env file")
    # parser.add_argument("--mongo", dest="mongo", help="use mongo database")
    # parser.set_defaults(mongo=False)

    # args = parser.parse_args()
    # print(args)
    
    # if args.env is not None:
    #     config = dict(dotenv_values(args.env))
    
    config = dict(dotenv_values(".env"))
    
    # if args.mongo:
    #     from mongo_manager import MongoManager
    #     manager = MongoManager(config=config)
    # else:
    from file_manager import FileManager
    manager = FileManager()
    
    try:
        print("Bot running.")
        main_thread = threading.Thread(target=main, args=(config, manager,))
        main_thread.start()
        main_thread.join()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except Exception as e:
        from errors import Errors
        errors = Errors()
        errors.save(os.path.basename(__file__), e)

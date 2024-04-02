from dotenv import dotenv_values
from telegram import Telegram
from scraper import Scraper
import argparse
import logging
import asyncio
import os

async def async_task(config: dict[str, str | None], database: str, url: str, hours: str):
    # TODO: change the mongodb logic...
    # if args.mongo:
    #     from mongo_manager import MongoManager
    #     manager = MongoManager(config=config)
    # else:
    from file_manager import FileManager
    manager = FileManager(database)
    manager.create_database()

    scraper = Scraper(url=url, hours=hours)
    bot = Telegram(config=config)

    while True:
        if manager.check_and_update(scraper.get_data()):
            await bot.send_message(chat_id=config["CHAT_ID"], text=f'<b>Nuovi Avvisi Disponibili:</b>\n{url}')
        await asyncio.sleep(float(hours) * 3600)

async def main(config: dict[str, str | None], urls_dict: dict[int, dict[str, str]]):
    tasks = []
    for _, value in urls_dict.items():
        database = str(value["database"])
        url = str(value["url"])
        hours = str(value["hours"])
        tasks.append(asyncio.create_task(async_task(config, database, url, hours)))
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", dest="env", required=True, help="set environment variables with \".env\" file.")
    # parser.add_argument("--mongo", dest="mongo", required=False, help="use mongodb database.")
    parser.add_argument("--urls", dest="urls", required=True, help="sets the file containing the URLs and the time to wait for each subsequent check.")
    parser.add_argument("--json", dest="json", required=False, help="get a database structure.")
    parser.set_defaults(env=None, mongo=False, urls=None, json=None)

    args = parser.parse_args()
    # print(args)
    
    if args.env is not None and os.path.exists(args.env):
        config = dict(dotenv_values(args.env))
    
    if args.urls is not None:
        urls_filename = str(args.urls)
        urls_dict = {}
        with open(urls_filename, "r") as file:
            for idx, line in enumerate(file.readlines(), start=1):
                tmp = line.split(",")
                # print(f"tmp: {tmp}")
                if len(tmp) != 3:
                    print(f"The {urls_filename} file was not configured correctly.")
                    os._exit(1)
                urls_dict[idx] = {"database": tmp[0], "url": tmp[1], "hours": tmp[2][:1]}
            
            # for key, value in urls_dict.items():
            #     print(f"db_filename: {key}, (url, hours): {value}")
            
            if args.json is not None:
                import json
                json_filename = f"./db/{args.json}"
                with open(json_filename, "w") as json_file:
                    json.dump(urls_dict, json_file)

    try:
        print("Bot running.")
        asyncio.run(main(config, urls_dict))
    except KeyboardInterrupt:
        print("\nExiting...")
        os._exit(0)
    except Exception:
        logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logger = logging.getLogger(__name__)
        logger.exception("An error occurred:")
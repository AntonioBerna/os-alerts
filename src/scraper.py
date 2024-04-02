import requests
import logging

class Scraper:
    def __init__(self, url: str, hours: str) -> None:
        self.url = url
        self.hour = float(hours)

    def get_data(self) -> str:
        try:
            return requests.get(url=self.url).text
        except Exception:
            logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception("An error occurred:")

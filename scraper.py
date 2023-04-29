import requests
import os

class Scraper:
    def __init__(self, config: dict) -> None:
        self.url = config["URL_2023"]
        self.hour = float(config["HOUR"])

    def get_data(self) -> str:
        try:
            return requests.get(url=self.url).text
        except Exception as e:
            from errors import Errors
            errors = Errors()
            errors.save(os.path.basename(__file__), e)

import requests

class Scraper:
    def __init__(self, config: dict) -> None:
        self.url = config["URL_2023"]
        self.hour = float(config["HOUR"])

    def get_data(self) -> str:
        return requests.get(url=self.url).text

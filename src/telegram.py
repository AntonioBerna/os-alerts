import requests
import logging

class Telegram:
    def __init__(self, config: dict) -> None:
        self.token = config["TOKEN"]
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        
    async def send_message(self, chat_id: str, text: str) -> None:
        payload = {"chat_id": chat_id, "parse_mode": "HTML", "text": text}
        try:
            requests.get(f"{self.api_url}/sendMessage", params=payload)
        except Exception:
            logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception("An error occurred:")

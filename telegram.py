import requests

class Telegram:
    def __init__(self, config: dict) -> None:
        self.token = config["TOKEN"]
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        
    def send_message(self, chat_id: str, text: str) -> None:
        payload = {"chat_id": chat_id, "parse_mode": "HTML", "text": text}
        try:
            requests.get(f"{self.api_url}/sendMessage", params=payload)
        except Exception as e:
            from errors import Errors
            errors = Errors()
            errors.save("telegram.py", e)



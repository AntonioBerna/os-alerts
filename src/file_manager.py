from pathlib import Path
import logging

class FileManager:
    def __init__(self, database: str) -> None:
        self.database = f".{database}"
        self.file_path = Path(f"./db/{self.database}")

    def create_database(self) -> None:
        try:
            if not self.file_path.exists():
                self.file_path.touch()
        except Exception as e:
            logging.exception("An error occurred:")

    def check_and_update(self, html: str) -> bool:
        try:
            data = str(len(html))
            with open(self.file_path, "r+") as file:
                if file.read().strip() == data: return False
                file.seek(0)
                file.write(data)
                file.truncate()
            return True
        except Exception:
            logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception("An error occurred:")
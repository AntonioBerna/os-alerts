from pathlib import Path

class FileManager:
    def __init__(self) -> None:
        self.database = "database"

    def check_and_update(self, html: str) -> bool:
        file_path = Path(self.database)
        if not file_path.exists():
            file_path.touch()            
        data = str(len(html))
        with open(self.database, "r+") as file:
            if file.read().strip() == data: return False
            file.seek(0)
            file.write(data)
            file.truncate()
        return True

class FileManager:
    def __init__(self) -> None:
        self.database = "database"

    def check_and_update(self, html: str) -> bool:
        data = str(len(html))
        with open(self.database, "r+") as file:
            if file.readline() == data:
                return False
            file.write(data)
        return True
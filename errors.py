class Errors:
    def __init__(self) -> None:
        self.errors_file = "log.txt"

    def save(self, filename: str, e: Exception) -> None:
        with open(self.errors_file, "a") as file:
            file.write(f"{filename}: {e}\n")
        print(f"\n{self.errors_file} has been updated.")
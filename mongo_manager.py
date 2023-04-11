import pymongo

class MongoManager:
    def __init__(self, config: dict) -> None:
        self.username = config["USERNAME"]
        self.password = config["PASSWORD"]
        self.cluster = config["CLUSTER"]
        self.session = config["SESSION"]

        try:
            self.link = f"mongodb+srv://{self.username}:{self.password}@{self.cluster}.{self.session}.mongodb.net/?retryWrites=true&w=majority"
            self.client = pymongo.MongoClient(self.link)
        except Exception as e:
            from errors import Errors
            errors = Errors()
            errors.save("mongo_manager.py", e)

    def get_database_list(self) -> list[str]:
        return self.client.list_database_names()

    def get_collections_list(self) -> list[str]:
        return self.client.telegram.list_collection_names()
    
    def check_and_update(self, html: str) -> bool:
        search = self.client.telegram.html.find_one({"length": {"$exists": True}})
        if search != None and search["length"] != str(len(html)):
            search["length"] = str(len(html))
            self.client.telegram.html.update_one({"_id": search["_id"]}, {"$set": search})
            return True
        return False

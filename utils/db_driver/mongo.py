import pymongo
DB_NAME = 'weather'


class MongoDbConnection(object):
    def __init__(self):
        self.mongo_client = None
        self.database = None
        if not self.mongo_client:
            self.mongo_client = pymongo.MongoClient('localhost', 27017)
            self.database = self.mongo_client[DB_NAME]

    def get_conn(self):
        return self.database

    def __del__(self):
        del self.mongo_client
        del self.database

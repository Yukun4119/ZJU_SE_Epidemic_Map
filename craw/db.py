# 这里可能会报错，其实是是误报
from pymongo import MongoClient

# 这里是本地的mongo数据库
uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
db = client['COVID-19_ZJU_SE_PROJECT']  

class DB:
    def __init__(self):
        self.db = db

        # 涉及插入和查找
    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)

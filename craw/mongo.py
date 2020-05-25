# 这里可能会报错，其实是是误报
from pymongo import MongoClient

# 这里是我本地的mongo数据库
# 在这之前需要先下载安装好mongo
uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
#建立名为COVID-19_ZJU_SE_PROJECT的数据库
db = client['COVID-19_ZJU_SE_PROJECT']  

class mongo_db:
    def __init__(self):
        self.db = db
    # 只是涉及插入和查找
    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)

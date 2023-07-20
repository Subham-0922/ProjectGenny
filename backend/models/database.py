from pymongo import MongoClient
client = MongoClient('mongodb+srv://ksubham789:Tesla132@cluster0.vfkl0dt.mongodb.net/?retryWrites=true&w=majority')
db = client['PROJECTJENNY']
user = db['users']
projects=db['projects']
tasks=db['tasks']
resource=db['resources']
activeUser=db['activeUser']
count=db['counter']
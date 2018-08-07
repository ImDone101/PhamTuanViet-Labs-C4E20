from pymongo import MongoClient

mongo_uri = "mongodb://admin:phamtuanviet1998@ds159100.mlab.com:59100/c4elabs"

# 1. Connect to Database
client = MongoClient(mongo_uri)

# 2. Get Database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# 4. Create a document
new_game = {
    "title" : "WOW",
    "description" : "World of Warcraft"
}

# 5. Insert document into collection
games.insert_one(new_game)

# 6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game['title'])
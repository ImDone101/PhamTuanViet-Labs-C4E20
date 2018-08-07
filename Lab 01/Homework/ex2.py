from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

noi_dung = 'Those who cannot remember the past are condemned to repeat it.'
posts = db['posts']
new_post = {
    "title" : "A random quote",
    "author" : "Viet Pham A.K.A Anzu",
    "content" : noi_dung
}

posts.insert_one(new_post)
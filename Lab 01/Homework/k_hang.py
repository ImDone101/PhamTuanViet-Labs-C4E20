from pymongo import MongoClient
import matplotlib
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']
all_khach = customers.find()

refs = {
    'Truyen mieng' : 0,
    'Quang cao' : 0,
    'Su kien' : 0
}

for khach in all_khach:
    if khach['ref'] == 'wom':
        refs['Truyen mieng'] += 1
    elif khach['ref'] == 'ads':
        refs['Quang cao'] += 1
    elif khach['ref'] == 'events':
        refs['Su kien'] += 1

for key, value in refs.items():
    print("So khach {} : {}".format(key, value))

pyplot.pie(refs.values(), labels= refs.keys())
pyplot.axis('equal')
pyplot.show()
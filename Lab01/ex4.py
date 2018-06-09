from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database

db = client.get_default_database()

# 3. Create collection

customers = db['customers']


# 4. Create document


# 5. Insert document into collection


all_customer = customers.find()

e = a = w = 0
for customer in all_customer:
    if customer['ref'] == 'events':
        e += 1
    elif customer['ref'] == 'ads':
        a += 1
    else:
        w += 1
print(e,w,a)


import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#1. Prepare data

labels = ['events', 'wom', 'ads']

values = [e,w,a]

colors = ["red", "blue", 'yellow']

# explode = [0,0,0,0.2]
#2. Plot

pyplot.pie(values, labels = labels, colors = colors)
pyplot.axis("equal")
#3. Show

pyplot.show()
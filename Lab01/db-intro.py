from pymongo import MongoClient

mongo_uri = 'mongodb://manhcuong_01:159357456258ccc@ds035593.mlab.com:35593/c4e18-manhcuong'

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database

db = client.get_default_database()

# 3. Create collection

games = db['games']

films = db['films']

# 4. Create document

# new_game = {
#     'title': "đá kiện",
#     'description' : 'chất vl'
# }

# new_film = {
#     "ten phim" : "Jav",
#     "noi dung" : "lành mạnh"
# }


# 5. Insert document into collection

# games.insert_one(new_game)
# films.insert_one(new_film)

all_game = games.find()

for game in all_game:
    print(game)
import pymongo
import certifi 

con_str = "mongodb+srv://FSDICh30:PassFSDICh30@cluster0.mzaem.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("OrganikaCh32")


me = {
    "first": "Frank",
    "last": "Sharper",
    "age": 40,
    "hobbies": [],
    "address": {
        "street": "Stylus",
        "number": 1993,
        "city": "Chula Vista"
    }
}
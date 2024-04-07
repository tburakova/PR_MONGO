from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:user1@atlascluster.jyaja7o.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['cats_database']
collection = db['cats']
db = client.ds01


# Create (створення нового документа)
def create_cat(name, age, features):
    cat_data = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat_data)
    print(f"Cat {name} added with id: {result.inserted_id}")

# Read (читання даних)
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat with name {name} not found")

# Update (оновлення даних)
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Age of cat {name} updated successfully")
    else:
        print(f"Cat with name {name} not found")

def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print(f"New feature added to cat {name}")
    else:
        print(f"Cat with name {name} not found")

# Delete (видалення даних)
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Cat {name} deleted successfully")
    else:
        print(f"Cat with name {name} not found")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"{result.deleted_count} cats deleted")

# Приклади використання функцій
if __name__ == "__main__":
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    
    read_all_cats()
    read_cat_by_name("barsik")
    
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "грає з м'ячиком")
    
    delete_cat_by_name("barsik")
    delete_all_cats()
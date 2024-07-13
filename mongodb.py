from pymongo import MongoClient
from urllib.parse import quote_plus

# Параметри підключення
username = "Arbenon"
password = "1G2d4Mongodb"

# Екранування паролю
encoded_password = quote_plus(password)

# Формування URI підключення
uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.mayr5kg.mongodb.net/"

# Підключення до MongoDB Atlas
client = MongoClient(uri)

# Створення бази даних
db = client["cats_db"]

# Створення колекції
collection = db["cats"]

# Читання (Read)
def get_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error: {e}")

def get_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"Error: {e}")

# Оновлення (Update)
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Updated cat {name}'s age to {new_age}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"Error: {e}")

def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Added feature '{new_feature}' to cat {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"Error: {e}")

# Видалення (Delete)
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat with name: {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"Error: {e}")

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except Exception as e:
        print(f"Error: {e}")

# Додавання нового кота (Create)
def add_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Added cat with id: {result.inserted_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Приклади використання функцій
    add_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    get_all_cats()
    get_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить гратися")
    delete_cat_by_name("barsik")
    delete_all_cats()

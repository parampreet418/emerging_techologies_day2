import pymongo
import ssl


def connect_to_mongodb():
    connection_string = "mongodb+srv://param:admin@cluster0.ylwpy.mongodb.net/sample_restaurants?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string, ssl_cert_reqs=ssl.CERT_NONE)
    # print(mongo_client)
    db = my_client["sample_restaurants"]
    columns = {"restaurant_id", "name", "borough", "cuisine"}
    # print(db.list_collection_names())
    restaurants_collection = db["restaurants"]
    # result = restaurants_collection.find({"cuisine": "American"})
    # result = restaurants_collection.find() #Returns all records
    # result = restaurants_collection.find_one() # Return only first record
    # result = restaurants_collection.find({}, columns)
    # Returns all records having column listed Bombay Masala
    result = restaurants_collection.find({"$or": [{"cuisine": "Chinese"}, {"cuisine": "Indian"}]}, columns).sort("borough").limit(50)
    result = restaurants_collection.find({"$and": [{"cuisine": "Indian"}, {"borough": "Brooklyn"}]}, columns).sort("borough").limit(50)
    result = restaurants_collection.find({}, columns).sort("name", 1)
    result = restaurants_collection.find({"cuisine": "Indian"}, columns)
    for row in result:
        print(row)

    # Insert Records
    connection_customer = db["customer"]
    dict = {"name": "Parampreet Kaur Gill", "id": "796418", "address": "Punjab, India"}
    x = connection_customer.insert_one(dict)
    customer_collection = db["customer"]
    results = customer_collection.find()
    for row in results:
        print(row)


if __name__ == '__main__':
    connect_to_mongodb()

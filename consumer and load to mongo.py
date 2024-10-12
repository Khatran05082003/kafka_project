from confluent_kafka import Consumer
import json
from pymongo import MongoClient


mongo_client = MongoClient('mongodb://localhost:27017/')  
db = mongo_client['glamira']  
collection = db['product_view']  

consumer_conf = {
    'bootstrap.servers': 'localhost:9194',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe(['new_product_view'])

try:
    while True:
        msg = consumer.poll(1.0)  
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        
        data = msg.value().decode('utf-8')
        json_data = json.loads(data)

        
        collection.insert_one(json_data)
        print(f"Received and saved message to MongoDB: {json_data}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    mongo_client.close()  
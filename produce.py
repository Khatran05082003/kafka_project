from confluent_kafka import Consumer, Producer
import json


consumer_conf = {
    'bootstrap.servers': '113.160.15.232:9094,113.160.15.232:9194,113.160.15.232:9294',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'kafka',
    'sasl.password': 'UnigapKafka@2024',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}


consumer = Consumer(consumer_conf)
consumer.subscribe(['product_view'])


producer_conf = {
    'bootstrap.servers': 'localhost:9194',  
}

producer = Producer(producer_conf)
new_topic = 'new_product_view'  

def delivery_report(err, msg):
       if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

try:
    while True:
        msg = consumer.poll(1.0)  
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        
        data = msg.value().decode('utf-8')
        print(f"Received message: {data}")

        
        producer.produce(new_topic, key=msg.key(), value=data, callback=delivery_report)
        producer.flush()

except KeyboardInterrupt:
    pass
finally:
    consumer.close()

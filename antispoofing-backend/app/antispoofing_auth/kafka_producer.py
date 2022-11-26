import socket

from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, topic) -> None:
        self.topic = topic
        self.conf_producer = {
            "bootstrap.servers": "kafka1:19092",
            "client.id": socket.gethostname(),
        }
        self.producer = Producer(self.conf_producer)

    def produce(self, message):
        print(f"Producing message to Kafka. Topic: {self.topic}. Message: {message}")
        self.producer.produce(self.topic, key=None, value=message)
        self.producer.flush()

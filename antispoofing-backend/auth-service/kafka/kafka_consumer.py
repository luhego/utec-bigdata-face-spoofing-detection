import json
import time

from confluent_kafka import Consumer, TopicPartition

from utils.authenticator import Authenticator

FILTERED_TOPIC = "filtered"


class KafkaConsumer:
    def __init__(self) -> None:
        self.conf = {
            "bootstrap.servers": "kafka1:19092, kafka2:19093, kafka3:19094",
            "group.id": "test1",
            "enable.auto.commit": "false",
            "auto.offset.reset": "earliest",
            "max.poll.interval.ms": "500000",
            "session.timeout.ms": "120000",
            "request.timeout.ms": "120000",
        }

    def consume(self, topic):
        self.consumer = Consumer(self.conf)
        self.topic = topic
        self.consumer.subscribe([self.topic])

        authenticator = Authenticator()

        try:

            while True:
                print(f"Consuming messages from Kafka topic: {self.topic}")
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue

                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    continue

                event = json.loads(msg.value().decode("utf-8"))
                partition = msg.partition()
                offset = msg.offset()

                print(f"Received message: {event}")

                authenticator.authenticate(event)

                self.consumer.commit(
                    offsets=[
                        TopicPartition(
                            self.topic, partition=partition, offset=offset + 1
                        )
                    ],
                    asynchronous=False,
                )

                time.sleep(2)

        except Exception as e:
            print(f"Exception: {e}")

        self.consumer.close()

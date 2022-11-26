import random
import json

SUCCESS_TOPIC = "checked"
FAILURE_TOPIC = "celery"

from kafka_producer import KafkaProducer


class Authenticator:
    def authenticate(self, event):
        print("Authenticate user using first_video and any video.")
        username = event.get("username")
        first_video = event.get("first_video")
        any_video = event.get("any_video")

        # TODO: add logic to authenticate user using first_video and any_video
        if random.random() < 0.5:
            print(
                f"Authentication succeeded. Producing message to Kafka. Topic: {SUCCESS_TOPIC}. Message: {event}"
            )
            kakfa_producer = KafkaProducer(SUCCESS_TOPIC)
            kakfa_producer.produce(json.dumps(event))
        else:
            print(
                f"Authenticaton failed. Producing message to Kafka. Topic: {FAILURE_TOPIC}. Message: {event}"
            )
            kakfa_producer = KafkaProducer(FAILURE_TOPIC)
            kakfa_producer.produce(json.dumps(event))

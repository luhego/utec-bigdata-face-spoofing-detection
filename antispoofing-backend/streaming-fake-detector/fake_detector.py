import random
import json

SUCCESS_TOPIC = "filtered"
FAILURE_TOPIC = "celery"

from kafka_producer import KafkaProducer


class StreamingFakeDetector:
    def detect(self, event):
        print("Detecting if video is real or fake.")
        username = event.get("username")
        video = event.get("first_video") or event.get("any_video")

        # TODO: add logic to detect fake videos
        if random.random() < 0.5:
            print(
                f"Real video. Producing message to Kafka. Topic: {SUCCESS_TOPIC}. Message: {event}"
            )
            kakfa_producer = KafkaProducer(SUCCESS_TOPIC)
            kakfa_producer.produce(json.dumps(event))
        else:
            print(
                f"Fake video. Producing message to Kafka. Topic: {FAILURE_TOPIC}. Message: {event}"
            )
            kakfa_producer = KafkaProducer(FAILURE_TOPIC)
            kakfa_producer.produce(json.dumps(event))

import random
import json

SUCCESS_TOPIC = "filtered"
FAILURE_TOPIC = "celery"

from kafka.kafka_producer import KafkaProducer
from .video_pipeline import VideoPipeline


class StreamingFakeDetector:
    def __init__(self) -> None:
        self.video_pipeline = VideoPipeline()

    def detect(self, event):
        print("Detecting if video is real or fake.")
        video = event.get("first_video") or event.get("any_video")

        is_real = self.video_pipeline.process(video) == 0
        if is_real:
            print(
                f"Real video. Producing message to Kafka. Topic: {SUCCESS_TOPIC}. Message: {event}"
            )
            # kakfa_producer = KafkaProducer(SUCCESS_TOPIC)
            # kakfa_producer.produce(json.dumps(event))
        else:
            print(
                f"Fake video. Producing message to Kafka. Topic: {FAILURE_TOPIC}. Message: {event}"
            )
            # kakfa_producer = KafkaProducer(FAILURE_TOPIC)
            # kakfa_producer.produce(json.dumps(event))

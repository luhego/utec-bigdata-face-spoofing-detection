import random
import json

SUCCESS_TOPIC = "checked"
FAILURE_TOPIC = "celery"

from kafka.kafka_producer import KafkaProducer
from .video_downloader import VideoDownloader
from .frame_extractor import FrameExtractor
from .frames_comparator import FramesComparator


class Authenticator:
    def authenticate(self, event):
        print("Authenticate user using first_video and any video.")
        first_video = event.get("first_video")
        any_video = event.get("any_video")

        if not first_video or not any_video:
            print("Signup Event. Ignore it.")
            return

        # Download videos
        video_downloader = VideoDownloader()
        video_downloader.download(first_video)
        video_downloader.download(any_video)

        # Extract frames
        frame_extractor = FrameExtractor()
        frames_first = frame_extractor.extract(first_video)
        frames_any = frame_extractor.extract(any_video)

        # Compare frames and detect if they belong to the same person
        are_same_person = FramesComparator().compare(frames_first, frames_any)

        if are_same_person:
            print(
                f"Authentication succeeded. Producing message to Kafka. Topic: {SUCCESS_TOPIC}. Message: {event}"
            )
            # kakfa_producer = KafkaProducer(SUCCESS_TOPIC)
            # kakfa_producer.produce(json.dumps(event))
        else:
            print(
                f"Authenticaton failed. Producing message to Kafka. Topic: {FAILURE_TOPIC}. Message: {event}"
            )
            # kakfa_producer = KafkaProducer(FAILURE_TOPIC)
            # kakfa_producer.produce(json.dumps(event))

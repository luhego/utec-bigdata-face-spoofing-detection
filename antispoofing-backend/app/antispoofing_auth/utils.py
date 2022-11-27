import secrets
import json

from django.contrib.auth import get_user_model

from .models import LoginAttempt
from .kafka_producer import KafkaProducer

User = get_user_model()


kafka_producer = KafkaProducer("loginattempt")


def create_user_account(username, email, password, **extra_fields):
    video = extra_fields.pop("video", None)
    video, video_hex_code = process_video(video)
    genre = extra_fields.get("genre", None)
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        genre=genre,
        video=video,
        video_hex_code=video_hex_code,
    )

    kafka_producer.produce(
        json.dumps({"username": username, "first_video": video.name, "any_video": ""})
    )

    return user


def register_login_attempt(**extra_fields):
    user = extra_fields.pop("user", None)
    video = extra_fields.pop("video", None)
    video, video_hex_code = process_video(video)
    LoginAttempt.objects.create(
        user=user, success=True, video=video, video_hex_code=video_hex_code
    )

    kafka_producer.produce(
        json.dumps(
            {
                "username": user.username,
                "first_video": user.video.name,
                "any_video": video.name,
            }
        )
    )

    return user


def process_video(video):
    video_hex_code = secrets.token_hex(32)
    video_name = video._get_name()
    video_extension = video_name.split(".")[-1]
    video._set_name(f"{video_hex_code}.{video_extension}")
    return video, video_hex_code

import json

from django.contrib.auth import get_user_model

from .models import LoginAttempt
from .kafka_producer import KafkaProducer

User = get_user_model()


kafka_producer = KafkaProducer("loginattempt")


def create_user_account(username, email, password, **extra_fields):
    video_s3_url = extra_fields.pop("video_s3_url", None)
    genre = extra_fields.get("genre", None)
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        genre=genre,
        video_s3_url=video_s3_url,
    )

    kafka_producer.produce(
        json.dumps({"username": username, "first_video": video_s3_url, "any_video": ""})
    )

    return user


def register_login_attempt(**extra_fields):
    user = extra_fields.pop("user", None)
    video_s3_url = extra_fields.pop("video_s3_url", None)
    LoginAttempt.objects.create(user=user, success=True, video_s3_url=video_s3_url)

    kafka_producer.produce(
        json.dumps(
            {
                "username": user.username,
                "first_video": user.video_s3_url,
                "any_video": video_s3_url,
            }
        )
    )

    return user

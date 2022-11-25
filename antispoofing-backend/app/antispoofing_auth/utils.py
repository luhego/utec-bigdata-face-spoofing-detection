import secrets
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


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
    return user


def process_video(video):
    video_hex_code = secrets.token_hex(32)
    video_name = video._get_name()
    video_extension = video_name.split(".")[-1]
    video._set_name(f"{video_hex_code}.{video_extension}")
    return video, video_hex_code

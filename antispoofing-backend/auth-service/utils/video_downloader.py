import boto3
import environ

env = environ.Env()
environ.Env.read_env()

BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
FOLDER_NAME = "files"

s3 = boto3.client(
    "s3",
    aws_access_key_id=env("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"),
    region_name=env("AWS_S3_REGION_NAME"),
)


class VideoDownloader:
    def download(self, video):
        print(f"Downloading video: {video}")
        video = video.split("/")[-1]
        video_path = f"{FOLDER_NAME}/{video}"
        s3.download_file(BUCKET_NAME, video, video_path)
        return video_path

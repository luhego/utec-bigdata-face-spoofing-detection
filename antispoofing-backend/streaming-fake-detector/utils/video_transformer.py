FOLDER_NAME = "files"

import ffmpeg


class VideoTransformer:
    def process(self, video):
        video_path, _ = video.split(".")
        video_path = f"{video_path}.avi"
        print(f"Transforming video: {video} to {video_path}.")
        stream = ffmpeg.input(video)
        stream = ffmpeg.output(stream, video_path, **{"qscale:v": 0})
        ffmpeg.run(stream, overwrite_output=True)

        return video_path

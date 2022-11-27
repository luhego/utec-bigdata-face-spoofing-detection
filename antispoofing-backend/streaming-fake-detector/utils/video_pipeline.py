from .video_downloader import VideoDownloader
from .video_preprocessor import VideoPreprocessor
from .video_loader import VideoLoader
from .video_predictor import VideoPredictor


class VideoPipeline:
    def __init__(self) -> None:
        self.processors = [
            VideoDownloader(),
            VideoPreprocessor(),
            VideoLoader(),
            VideoPredictor(),
        ]

    def process(self, video):
        output = video
        for processor in self.processors:
            output = processor.process(output)
        return output

import numpy as np
import cv2

IMG_SIZE = 256
NUM_FRAMES_PER_VIDEO = 16


def video2frames(video_path, resize=(IMG_SIZE, IMG_SIZE)):
    cap = cv2.VideoCapture(video_path)
    frames = []
    is_there_frame = True
    num_total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    resampling_rate = int(num_total_frames / NUM_FRAMES_PER_VIDEO)
    idf = 0
    while is_there_frame and len(frames) < NUM_FRAMES_PER_VIDEO:
        is_there_frame, frame = cap.read()
        if is_there_frame and idf % resampling_rate == 0:
            # grayscale
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, resize)
            # resize
            frames.append(frame)
        idf = idf + 1

    assert len(frames) == NUM_FRAMES_PER_VIDEO
    return np.array(frames)


class VideoPreprocessor:
    def process(self, video):
        print(f"Preprocessing video: {video}")
        dataset_x = []
        frames = video2frames(video)
        dataset_x = [*dataset_x, *frames]
        dataset_x = np.array(dataset_x)
        return dataset_x

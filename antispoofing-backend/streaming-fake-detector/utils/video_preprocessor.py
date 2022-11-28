import numpy as np
import cv2

IMG_SIZE = 256
NUM_FRAMES_PER_VIDEO = 16


def count_real_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    is_there_frame = True
    num_total_frames = 0
    while is_there_frame:
        is_there_frame, _ = cap.read()
        num_total_frames += 1
    return num_total_frames


def video2frames(video_path, resize=(IMG_SIZE, IMG_SIZE)):
    frames = []
    is_there_frame = True
    num_total_frames = count_real_frames(video_path)
    resampling_rate = int(num_total_frames / NUM_FRAMES_PER_VIDEO)
    idf = 0

    cap = cv2.VideoCapture(video_path)
    while is_there_frame and len(frames) < NUM_FRAMES_PER_VIDEO:
        is_there_frame, frame = cap.read()
        if is_there_frame and idf % resampling_rate == 0:
            # grayscale
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, resize)
            # resize
            frames.append(frame)
        idf = idf + 1

    print(num_total_frames, len(frames))
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

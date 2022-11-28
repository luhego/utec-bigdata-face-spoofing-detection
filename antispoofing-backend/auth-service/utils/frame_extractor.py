import cv2

FOLDER_NAME = "files"


class FrameExtractor:
    def extract(self, video):
        video = video.split("/")[-1]
        video_path = f"{FOLDER_NAME}/{video}"

        print(f"Extracting frames from video. {video_path}")
        cap = cv2.VideoCapture(video_path)
        frames = []
        ret = True
        while ret:
            ret, frame = cap.read()
            if ret == False:
                break

            frames.append(frame)

        cap.release()

        print(f"Numbef of frames extracted: {len(frames)}")

        return frames

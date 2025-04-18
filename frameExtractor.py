# Program To Read video
# and Extract Frames

import cv2

def video_to_frames(video_path, output_dir, frame_rate=30):
    """
    Extracts frames from a video and saves them as images.

    Args:
        video_path (str): Path to the input video file.
        output_dir (str): Path to the directory where frames will be saved.
        frame_rate (int, optional): Desired frame rate for extraction. Defaults to 30.
    """
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        raise Exception("Could not open video file.")

    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        if frame_count % int(video_capture.get(cv2.CAP_PROP_FPS) / frame_rate) == 0:
            output_path = f"{output_dir}/frame_{frame_count:04d}.jpg"
            cv2.imwrite(output_path, frame)
        frame_count += 1

    video_capture.release()
    print(f"Extracted {frame_count} frames to {output_dir}")

if __name__ == "__main__":
    video_file = "C:/Users/Yile0/Downloads/2024-12-08 23-32-20.mp4"
    output_directory = "C:/Users/Yile0/PycharmProjects/osutime/frames/map1"
    video_to_frames(video_file, output_directory)

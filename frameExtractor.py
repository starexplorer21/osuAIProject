# Program To Read video
# and Extract Frames

import cv2


# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)
    vidObj.open(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display the recording screen
        cv2.imshow('resized_gray', gray_frame)

        # Saves the frames with frame-count
        cv2.imwrite("C:\\Users\\Yile0\\PycharmProjects\\osutime\\frames\\map5\\%d.png" % count, gray_frame)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("C:\\Users\\Yile0\\Downloads\\2024-12-08 23-22-28.mp4")

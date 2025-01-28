from osrparse import Replay, parse_replay_data
import csv
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

# ok so for every frame I know the average time between a frame.
# let's just use that and then work it out from there.

map = "map1"

replay = Replay.from_path("C:\\Users\\Yile0\\Downloads\\"+ map + ".osr")

# time relative to game.
timer = 0

# First frame
# mass rename takes too much time, so I can just call frame 19 the
# first frame for ease.
# 130 for map 1
# 78 for map 2
FIRST = 160

# FPS of recording
FPS = 60

video_output = cv2.VideoWriter("dsync_video.avi",cv2.VideoWriter_fourcc(*'DIVX'), 60, (800, 600))

FOLDER_PATH = "C:/Users/Yile0/PycharmProjects/osutime/frames/"+ map + "/"

# toss the first one because it doesn't make any sense
data = replay.replay_data[2:len(replay.replay_data)-10]

print(len(data))

print(len(replay.replay_data))

output = []

dsyncs = []

frame_timer = FIRST
print(replay.replay_data[len(replay.replay_data)-1])

overhead = 0

for val in tqdm(range(0, len(data))):
    input = data[val]
    time = input.time_delta
    x = input.x
    y = input.y
    # disregard keys for now, playing with relax mode to
    # automate presses.

    # increment timer to current time.

    row = dict()
    row['x'] = x
    row['y'] = y

    # 1000 is ms in second.
    # this find the latests closest frame
    #
    # if val % 3 != 0:
    timer += time* 0.7333333333

    nearest_frame = int(timer // 16.6666)

    # show image with x y for lining up
    nearest_frame = 8891 if nearest_frame >= 8891 else nearest_frame
    img = np.asarray(Image.open(FOLDER_PATH + str(nearest_frame) + ".png").convert("L"))

    dsyncs.append(timer - math.floor((timer * 0.001) * FPS) * 23.0)

    frame = cv2.imread(FOLDER_PATH + str(nearest_frame) + ".png")

    frame = cv2.circle(frame,(int(x*1.5625),int(y*1.5625)),20, (0,255,0), -1)

    video_output.write(frame)

    # if there aren't enough frames, then pad with the first frame
    # this is because this case only arises for the first 4 inputs.

    for i in range(4):
        if nearest_frame - i > 0 and nearest_frame - i + FIRST < 8891:
            row['frame ' + str(4 - i)] = FOLDER_PATH + str(nearest_frame - i + FIRST) + ".png"
        elif nearest_frame - i + FIRST < 8891:
            row['frame ' + str(4 - i)] = FOLDER_PATH + str(nearest_frame - i + FIRST) + ".png"
        else:
            row['frame ' + str(4 - i)] = FOLDER_PATH + str(8891) + ".png"

    output.append(row)

video_output.release()

print(output[:10])


from osrparse import Replay, parse_replay_data
import csv
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

map = "map1"

replay = Replay.from_path("C:\\Users\\Yile0\\Downloads\\"+ map + ".osr")

# time relative to game.
timer = 0

# First frame
# mass rename takes too much time, so I can just call frame 19 the
# first frame for ease.
# 130 for map 1
# 78 for map 2
FIRST = 130

# FPS of recording
FPS = 120

video_output = cv2.VideoWriter("dsync_video.avi",cv2.VideoWriter_fourcc(*'DIVX'), 60, (800, 600))

FOLDER_PATH = "C:/Users/Yile0/PycharmProjects/osutime/frames/"+ map + "/"

# toss the first one because it doesn't make any sense
data = replay.replay_data[2:len(replay.replay_data)-10]

print(len(data))

print(len(replay.replay_data))

output = []

frames = []
print(replay.replay_data[len(replay.replay_data)-1])

for val in tqdm(range(0, len(data))):
    input = data[val]
    time = int(input.time_delta)
    output.append(timer)
    nearest_frame = math.floor(timer * 0.001 * FPS)*1000 / FPS
    frames.append(nearest_frame)
    timer += time

plt.plot(output)
plt.plot(frames, "g-")

plt.show()


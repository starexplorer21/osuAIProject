from osrparse import Replay, parse_replay_data
import csv
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

map = "map1"

replay = Replay.from_path("C:\\Users\\Yile0\\Downloads\\"+ map + ".osr")

# time relative to game.
timer = 0

# First frame
# mass rename takes too much time, so I can just call frame 19 the
# first frame for ease.
# 130 for map 1
# 78 for map 2
FIRST = 123

# FPS of recording
FPS = 60

FOLDER_PATH = "C:/Users/Yile0/PycharmProjects/osutime/frames/"+ map + "/"

# toss the first one because it doesn't make any sense
data = replay.replay_data[2:len(replay.replay_data)-10]

print(len(data))

print(len(replay.replay_data))

output = []

dsyncs = []
print(replay.replay_data[len(replay.replay_data)-1])

for val in range(0, len(data)):
    print(val)
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

    if val % 3 != 0:
        timer += time
    nearest_frame = math.floor((timer * 0.001) * FPS) + FIRST

    if val % 4 != 0:
        # show image with x y for lining up
        img = np.asarray(Image.open(FOLDER_PATH + str(nearest_frame) + ".png").convert("L"))

        dsyncs.append(timer - math.floor((timer * 0.001) * FPS) * 16.66666)

        plt.imshow(img)
        plt.plot(x * 1.5625 + 5, y * 1.5625 + 5, "bo")
        plt.show()


        # if there aren't enough frames, then pad with the first frame
        # this is because this case only arises for the first 4 inputs.

        for i in range(4):
            if nearest_frame - i > 0 and nearest_frame - i + FIRST < len(data):
                row['frame ' + str(4 - i)] = FOLDER_PATH + str(nearest_frame - i + FIRST) + ".png"
            elif nearest_frame - i + FIRST < 5348:
                row['frame ' + str(4 - i)] = FOLDER_PATH + str(FIRST) + ".png"
            else:
                row['frame ' + str(4 - i)] = FOLDER_PATH + str(8891) + ".png"

        output.append(row)

plt.plot(dsyncs)
plt.show()

print(output[:10])

fields = ['x', 'y', 'frame 4', 'frame 3', 'frame 2', 'frame 1']

filename = map + "_data.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()

    writer.writerows(output)

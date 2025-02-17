from osrparse import Replay, parse_replay_data
import csv
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

replay = Replay.from_path("C:\\Users\\Yile0\\Downloads\\"+ "map1" + ".osr")

for i in range(10):
    print(replay.replay_data[i])
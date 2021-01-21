import cv2
import numpy as np


def find_contours(binary):
    region = []
    # 查找轮廓
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        region.append(box)
    return region


def detect(gray):
    ret, binary = cv2.threshold(gray, 0, 205, cv2.THRESH_BINARY)
    region = find_contours(binary)
    return region

import cv2
import numpy as np
import common
import os

def imShowTest():
  template = cv2.imread('templates/tooth.high.png', 0)
  cv2.imshow('IMAGE', template)
  cv2.waitKey(0)


def main():
  cap = cv2.VideoCapture(u'data/CH0P0360.MPG')

  while (cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 200, 300)

    to_show = common.image_concat((gray, edges), (2, 2))
    cv2.imshow('demo', to_show)

    if cv2.waitKey(30) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
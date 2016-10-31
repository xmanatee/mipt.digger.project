import cv2
import numpy as np
import common
import os
import rectangle_builder
import detector

def imShowTest():
  template = cv2.imread('templates/tooth.high.png', 0)
  cv2.imshow('IMAGE', template)
  cv2.waitKey(0)


def main():
  cap = cv2.VideoCapture(u'data/CH0P0389.MPG')
  r_b = rectangle_builder.RectangleBuilder()

  while (cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 200, 300)

    lb, rt = r_b(edges)
    rectangle = np.empty_like(gray)
    rectangle[:] = gray

    cv2.rectangle(rectangle, lb, rt, (0, 200, 0), 2)
    print detector.Detector.get_probability(edges, lb, (lb[0], rt[1]))
    # print lb, rt
    to_show = common.image_concat((gray, edges, rectangle, gray), (2, 2))
    cv2.imshow('demo', to_show)

    if cv2.waitKey(30) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
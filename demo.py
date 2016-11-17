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
    # TODO(mivanov): resize is used because of constants in detector
    frame = cv2.resize(frame, (480, 640))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 200, 300)

    lb, rt = r_b(edges)
    rectangle = np.empty_like(gray)
    rectangle[:] = gray

    cv2.rectangle(rectangle, lb, rt, (0, 200, 0), 2)
    place_found = [None] * 5
    print detector.Detector.get_probability(edges, lb, (lb[0], rt[1]), place_found)

    teeth = np.empty_like(gray)
    teeth[:] = gray
    for pair in place_found:
      if pair is not None:
        cv2.rectangle(teeth, pair[0], pair[1], (0, 200, 0), 2)
    print place_found
    to_show = common.image_concat((teeth, edges, rectangle, gray), (2, 2))
    # to_show = cv2.resize(to_show, (720, 405))
    cv2.imshow('demo', to_show)

    if cv2.waitKey(30) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
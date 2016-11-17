import cv2
import rectangle_builder
import numpy as np

cap = cv2.VideoCapture(u'data/CH0P0389.MPG')
r_b = rectangle_builder.RectangleBuilder()

while(cap.isOpened()):
  ret, frame = cap.read()
  frame = cv2.resize(frame, (480, 640))
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 200, 300)
  lines = cv2.HoughLinesP(edges, 0.5, 0.01, threshold=15, minLineLength=25, maxLineGap=3)

  print lines.shape

  lines = lines[0]

  for x1, y1, x2, y2 in lines:
    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

  # for fr in q:
  #   for ch in fr:
  #     for c in ch[1]:
  #       cv2.rectangle(frame, (c[0], ch[0]), (c[1], ch[0]+1), (0,200,0))

  to_show = cv2.resize(edges, (720, 405))
  to_show_ = cv2.resize(frame, (720, 405))
  cv2.imshow('', to_show)
  cv2.imshow(' ', to_show_)

  if cv2.waitKey(30) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

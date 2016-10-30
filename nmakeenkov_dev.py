import cv2
import rectangle_builder

cap = cv2.VideoCapture(u'data/CH0P0389.MPG')
r_b = rectangle_builder.RectangleBuilder()

while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 200, 300)

  lb, rt = r_b(edges)

  cv2.rectangle(frame, lb, rt, (0, 200, 0), 2)


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

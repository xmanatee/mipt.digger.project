import numpy as np
import cv2

def toothHave(edges, xt, yt, sizex, sizey):
    good_contur = 0
    all_contur = sizex * 2 + sizey * 2
    for i in range(sizex):
        print type(edges[xt+i][yt])
        if (edges[xt + i][yt] == 255):
            good_contur += 1
        if (edges[xt + i][yt + sizey] == 255):
            good_contur += 1
    for j in range(sizey):
        if (edges[xt][yt + j] == 255):
            good_contur += 1
        if (edges[xt + sizex][yt + j] == 255):
            good_contur += 1
    return good_contur * 1.0 / all_contur

img = cv2.imread('test1.jpg')
edges = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges_one = np.where(edges > 20)
edges[edges_one] = 255
p1 = (353, 246)
p2 = (353, 359)

t1 = (293, 264)
t2 = (291, 281)
t3 = (290, 298)
t4 = (292, 317)
t5 = (294, 377)

percent_contur = [0.0, 0.0, 0.0, 0.0, 0.0]

while True:
    cv2.imshow('frame',edges)

    for num_tooth in range(5):
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for rec_dx in range(-2, 3):
                    for rec_dy in range(-2, 3):
                        xt = int(p1[0] - (p2[1] - p1[1]) * 60.0 / 113)
                        yt = int(p1[1] + (p2[1] - p1[1]) * 18.0 / 113) + int(num_tooth * (p2[1] - p1[1]) * 17.0 / 113)
                        sizex = int((p2[1] - p1[1]) * 26.0 / 113)
                        sizey = int((p2[1] - p1[1]) * 6.0 / 113)
                        percent_contur[num_tooth] = max(percent_contur[num_tooth], toothHave(edges, xt + dx, yt + dy, sizex + rec_dx, sizey + rec_dy))


    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

print percent_contur
cv2.destroyAllWindows()
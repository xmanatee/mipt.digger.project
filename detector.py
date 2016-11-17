import numpy as np
import cv2

class Detector:
    @staticmethod
    def tooth_have(edges, xt, yt, sizex, sizey):
        if sizex <= 0 or sizey <= 0:
            return 0
        good_contur = 0
        all_contur = sizex * 2 + sizey * 2
        for i in range(sizex):
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

    @staticmethod
    def get_probability(edges, p1, p2, place_found=None):
        print edges.shape
        percent_contur = [0.0, 0.0, 0.0, 0.0, 0.0]
        for num_tooth in range(5):
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    for rec_dx in range(-2, 3):
                        for rec_dy in range(-2, 3):
                            xt = int(p1[0] - (p2[1] - p1[1]) * 60.0 / 113)
                            yt = int(p1[1] + (p2[1] - p1[1]) * 18.0 / 113) + int(
                                num_tooth * (p2[1] - p1[1]) * 17.0 / 113)
                            sizex = int((p2[1] - p1[1]) * 26.0 / 113)
                            sizey = int((p2[1] - p1[1]) * 6.0 / 113)
                            current_result = Detector.tooth_have(edges, xt + dx, yt + dy,
                                    sizex + rec_dx, sizey + rec_dy)
                            if current_result > percent_contur[num_tooth]:
                                percent_contur[num_tooth] = current_result
                                if place_found is not None:
                                    place_found[num_tooth] = ((xt + dx, yt + dy),
                                        (xt + dx + sizex + rec_dx, yt + dy + sizey + rec_dy))
        return percent_contur

if __name__ == '__main__':
    img = cv2.imread('test1.jpg')
    edges = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges_one = np.where(edges > 20)
    edges[edges_one] = 255
    p1 = (353, 246)
    p2 = (353, 359)

    place_found = [None] * 5
    print Detector.get_probability(edges, p1, p2, place_found)
    print place_found

    while True:
        cv2.imshow('frame', edges)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
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
    def get_probability(edges, p1, p2):
        print p1, p2
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
                            percent_contur[num_tooth] = max(percent_contur[num_tooth],
                                    Detector.tooth_have(edges, xt + dx, yt + dy, sizex + rec_dx,
                                            sizey + rec_dy))
        return percent_contur

if __name__ == '__main__':
    img = cv2.imread('test1.jpg')
    edges = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges_one = np.where(edges > 20)
    edges[edges_one] = 255
    p1 = (353, 246)
    p2 = (353, 359)

    print Detector.get_probability(edges, p1, p2)
    cv2.destroyAllWindows()
import math
import numpy as np
import cv2


def make_kernel(size, sigma, lamda, theta, gamma):
    center = size // 2
    result = np.zeros((size, size))
    for i in range(-center, center+1):
        for j in range(-center, center+1):
            point = (i, j)
            x_ = point[0]*math.cos(theta)+point[1]*math.sin(theta)
            y_ = -point[0]*math.sin(theta)+point[1]*math.cos(theta)

            result[i+center, j+center] = math.exp(-(x_**2 + gamma**2 * y_**2) /
                                                  (2*sigma**2))*math.cos(2*math.pi*x_/lamda)

    return result


if __name__ == '__main__':
    kernel = make_kernel(5, 5, 10, 0, 0.5)

    img = cv2.imread("../assets/lena.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filter_img = cv2.filter2D(img, -1, kernel)
    cv2.imshow("original", img)
    cv2.imshow("filter", filter_img)

    cv2.waitKey(0)

import cv2 as cv
import matplotlib.pyplot as plt

path = r"E:\testdata\TEST\R0603_15um_green.bmp"

img = cv.imread(path, cv.IMREAD_COLOR)
# 新建可视化窗口
cv.namedWindow("title", flags=cv.WINDOW_NORMAL)


def nothing():
    pass


new_img = cv.inRange(img, (60, 60, 30), (255, 255, 255))


cv.imshow("title", new_img)
cv.waitKey(0)
# cv.createTrackbar('R', 'title', 20, 255, nothing)
# cv.createTrackbar('G', 'title', 20, 255, nothing)
# cv.createTrackbar('B', 'title', 20, 255, nothing)
# cv.createTrackbar('W', 'title', 0, 255, nothing)


retval, labels, stats, centroids = cv.connectedComponentsWithStats(new_img, connectivity=8)

print(retval)
print(labels)
print(stats)
print(centroids)
# plt.imshow(labels, cmap=plt.cm.gray)
# plt.show()
# 转成HSV图片
# img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# 二值化
# ret, img = cv.threshold(img, 60, 255, cv.THRESH_BINARY) #灰度图二值化


# while True:
#     cv.imshow('title', new_img)
#     k = cv.waitKey(10) & 0xff
#     if k == 27:
#         break
#     r = int(cv.getTrackbarPos('R', 'title'))
#     g = int(cv.getTrackbarPos('G', 'title'))
#     b = int(cv.getTrackbarPos('B', 'title'))
#     # w = int(cv.getTrackbarPos('W', 'title'))
#     new_img = cv.inRange(img, (b, g, r), (255, 255, 255))
# # cv.imshow('title',img)
# # cv.waitKey(1000)
# print(f"R:{r}  G:{g}  B:{b}")
# retval, labels, stats, centroids = cv.connectedComponentsWithStats(new_img)
# print(type(retval))
# print(type(labels))
# print(stats)
# print(type(centroids))
# plt.imshow(labels, cmap=plt.cm.gray)
# plt.show()


for stat in stats:
    cv.rectangle(img, (stat[0], stat[1]), (stat[0]+stat[2], stat[1]+stat[3]), (0, 255, 0),thickness=3)

cv.imshow('title', img)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2
img=cv2.imread("manireddy.jpeg",0)
cv2.imshow("image",img)
cv2.waitKey(500000)
cv2.destroyAllWindows()
import cv2
img = cv2.imread(r"C:\Users\minatu\Python_OpenCV\photo02.jpg")
cv2.imshow('OpenCV', img)
print(img.shape)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2

img = cv2.imread("me.jpg",1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# 1000 = width
# 500 = length
resize_image = cv2.resize(img,(100,100))
cv2.imshow("me",resize_image)
cv2.imwrite("RESIZED.jpg",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

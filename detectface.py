import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #create face cascade object

img = cv2.imread("image.jpeg")   #load an image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert original img (BGR img) into grayscale version for better accuracy


# to detect multiscale face in an img 
# give the coordinates of the face
# (scaleFactor = 1.5) and (minNeighbors = 5) are consider good for giving more accuracy
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.5,
minNeighbors = 5)

# draw the rectangle on face in an img
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

print(type(faces)) #type of face
print(faces) #print that face

re = cv2.resize(img,(img.shape[1],img.shape[0]))  #resize it
text = cv2.putText(re, 'OpenCV Demo', (120, 120), 
                   cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0, 0), 2)


cv2.imshow("gray",re)  # display 
cv2.waitKey(0) # waiting time for an img to be display for------> 0 used .pywhen you have to do manually, 2000 is for 2ms
cv2.destroyAllWindows() #destroy after time period is over 

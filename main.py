import cv2, time, pandas
from datetime import datetime

first_frame = None
stat_list = [None,None] 
times = []
df = pandas.DataFrame(columns = ["Start","End"])

video = cv2.VideoCapture(0)
 
while True:
    """
    FOR CHECKING IF THERE IS FRAME OR NOT
    IF TRUE PRINT NUMPY ARRAY OF FRAME 
    """
    check, frame = video.read()
    status = 0 
    # CONVERTING BGR IMAGE TO GRAY SCALE FOR ACCURACY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    # IF FIRST FRAME IS STILL NONE ASSIGN GRAY TO TO IT 
    if first_frame is None:
        first_frame = gray
        continue
    """
    THE DIFFERENCE BETWEEN FIRST FRAME AND UPCOMING FRAME IS IN DELTA FRAME,
    THRESH FRAME IS TO GIVE A COMMAND FOR SPECIFIC PIXEL NEEDS TO BE DISPLAYED ACC. TO GIVEN VALUE
    USING THRESH_BINARY METHOD WHICH RETURNS A TUPLE 
    """

    delta_frame = cv2.absdiff(first_frame, gray)     
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)             #TO REMOVE SHADOWS FROM CAPTURES WE USE DILATE METHOD 

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    stat_list.append(status)
    if stat_list[-1] == 1 and stat_list[-2] == 0:
        times.append(datetime.now())
    if stat_list[-1] == 0 and stat_list[-2] == 1 :
        times.append(datetime.now())

    """
    SHOWING ALL THE FRAMES WEBCAM CAPTURES
    """    
    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame",frame )

    #  KEY IS ASSIGN TO WAIT FOR DISPLAYING AN IMAGE
    key = cv2.waitKey(1)
    

    # TO COME OUT OF A LOOP
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(stat_list)
print(times)

for i in range(0,len(times),2):
    df = df.append({"Start": times[i],"End": times[i+1]},ignore_index=True)

df.to_csv("a.csv")

time.sleep(1)
video.release()
cv2.destroyAllWindows
import cv2
import numpy as np
import datetime

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strin = f"{x}, {y}"
        print(strin)
        cv2.putText(frame, strin, (x,y), FONT, 1,(0,255,0),2)
        cv2.imshow("Frame",frame)
    if event == cv2.EVENT_RBUTTONDOWN:
        bgr = str(img[x,y])
        print(bgr)
        cv2.putText(frame, bgr, (x,y), FONT, 1,(0,255,0),2)
        cv2.imshow("Frame",frame)


cap = cv2.VideoCapture(0)
img = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED) #const -1
zero_img = np.zeros([512,512,3], np.uint8)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (960,540))

img = cv2.line(img,(0,0),(255,255),(255,0,0),10)
img = cv2.arrowedLine(img,(255,255),(0,255),(0,255,0),5)
img = cv2.rectangle(img,(255,255),(540,540),(0,0,255),3)
img = cv2.rectangle(img,(540,255),(540,540),(0,0,150),-1)
img = cv2.circle(img,(255,150),(150,255),(150,0,0),5)
img = cv2.circle(img,(255,0),(0,255),(150,0,0),-1)
FONT = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Open CV", (0,255), FONT, 4, (0,150,0), 5, cv2.LINE_AA)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #Height is cont 4
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #Width is const 3

cv2.imshow("img", img)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,768)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1024)


while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = f"Width: {width}\nHeight: {height}"
    date = str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (10,50), FONT, 5, (255,0,0), 5,cv2.LINE_AA)
    frame = cv2.putText(frame, date, (10,60), FONT, 1, (255,0,0), 5,cv2.LINE_AA)
    if ret == True:
        cv2.imshow("Frame", frame)
        cv2.imshow("gray", gray)

        out.write(frame)
        cv2.setMouseCallback('Frame',)
        k = cv2.waitKey(0) #fps, actually delays x ms, 0 for frame freeze
        if k == ord('s'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
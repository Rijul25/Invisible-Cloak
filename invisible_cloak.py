import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        red = np.uint8([[[0,0,255]]]) #bgr value of red
        hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        #lower:hue-10,100,100
        #higher:h+10,255,255
        #we are saying jo bhi color is range mei aaenge,
        #disapppear them 
        #print(hsv_red)
        #threshold the hsv values to get red
        #here hue =0 as print hsv mei aaya tha
        #0,255,255
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])
        mask = cv2.inRange(hsv,l_red,u_red)
        
        #cv2.imshow("mask",mask)
        #part1 is all things red
        part1 = cv2.bitwise_and(back,back,mask = mask)
        #cv2.imshow("part1",part1)#ignore everything of red
        
        mask = cv2.bitwise_not(mask)
        
        #part2 is all things not red
        part2 = cv2.bitwise_and(frame,frame,mask = mask)
        #cv2.imshow("mask",part2)
        
        cv2.imshow("cloak",part1 + part2) 
        
        if cv2.waitKey(5) == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()
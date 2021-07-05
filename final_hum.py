import Jetson.GPIO as GPIO
import numpy as np
import cv2
import cv2 as cv
import time
import math

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
out_a = 7
out_b = 13
out_c = 11
GPIO.setup(out_a,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(out_b,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(out_c,GPIO.OUT,initial=GPIO.LOW)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

end_time = time.time()
vcap = cv2.VideoCapture(0)
bi_ksize=15
threshold=25
sigma=10
if vcap.isOpened(): 
    width  = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    # or
    width  = vcap.get(3)  # float `width`
    height = vcap.get(4)  # float `height`

    print('width, height:', width, height)
    
    fps = vcap.get(cv2.CAP_PROP_FPS)
    # or
    fps = vcap.get(5)
    
    print('fps:', fps)  # float `fps`
    
    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    # or
    frame_count = vcap.get(7)
    
    print('frames count:', frame_count)  # float `frame_count`

    print('cv2.CAP_PROP_FRAME_WIDTH :', cv2.CAP_PROP_FRAME_WIDTH)   # 3
    print('cv2.CAP_PROP_FRAME_HEIGHT:', cv2.CAP_PROP_FRAME_HEIGHT)  # 4
    print('cv2.CAP_PROP_FPS         :', cv2.CAP_PROP_FPS)           # 5
    print('cv2.CAP_PROP_FRAME_COUNT :', cv2.CAP_PROP_FRAME_COUNT)   # 7



while True:
    ret, img = vcap.read()
    img = cv2.flip(img, 1)
    im_bi = cv2.bilateralFilter(img, bi_ksize, sigma, sigma)
    box, weights = hog.detectMultiScale(im_bi, winStride=(8,8))
    box = np.array([[i, j, i+t, j+k] for (i,j,t,k) in box])
    for (x,y,w,h) in box:
        #print(len(faces))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        crop_img = im_bi[y:y+h, x:x+w]
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        thresholded = cv2.threshold(gray, threshold, 255, 0)[1]
        _,contours,hierarchy = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        area = cv.contourArea(cnt)
        rct = w*h
        abh = area/w*h
        ab = 100-(abh*0.001)
        cv2.putText(img,str(ab),(x, y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)
        if (x > 0 and x < 100) and (y > 0 and y < 160):
            data = "left upward "
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif x > 300 and (y > 0 and y < 160):
            data = "right Upward"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.HIGH)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
 
        elif (x > 100 and x < 300 ) and (y > 0 and y < 160):
            data = "upward"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif (x > 0 and x < 100 ) and (y > 160 and y <320):
            data = "left"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.HIGH) 
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif (x > 100 and x < 300) and (y > 160 and y < 320):
            data="Front"
            cv2.putText(img, str(data),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif x > 300 and (y > 160 and y < 320):
            data="right"
            cv2.putText(img, str(data),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.HIGH)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif (x > 0 and x < 100) and (y > 320 and y < 480):
            data = "left downward"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.HIGH)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif (x > 100 and x < 300) and (y > 320 and y < 480):
            data = "downward"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        elif (x > 300) and (y > 320 and y < 480):
            data = "right downward"
            cv2.putText(img,str(data),(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            if ab > -25 and ab < 60:
                rob = "near"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.HIGH)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            elif ab > 60 and ab < 100:
                rob = "accept"
                GPIO.output(out_a,GPIO.HIGH)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
            else:
                rob = "reject"
                GPIO.output(out_a,GPIO.LOW)
                GPIO.output(out_b,GPIO.LOW)
                GPIO.output(out_c,GPIO.LOW)
                cv2.putText(img,str(rob),(x, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 2)
        else:
            GPIO.output(out_a,GPIO.LOW)
            GPIO.output(out_b,GPIO.LOW)
            GPIO.output(out_c,GPIO.LOW)

   


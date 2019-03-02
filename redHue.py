import cv2
import numpy as np
import statistics as st

def indices(m,n):
    r0 = np.arange(m) # Or r0,r1 = np.ogrid[:m,:n], out[:,:,0] = r0
    r1 = np.arange(n)
    out = np.empty((m,n,2),dtype=int)
    out[:,:,0] = r0[:,None]
    out[:,:,1] = r1
    return out

def findNDraw(img2, hue, sF = 1, color = "red"):
    # img = cv2.imread(link, 1)
    img = cv2.resize(img2, (0, 0), fx =sF, fy=sF)

    shp = img.shape

    ind = np.array(indices(shp[0], shp[1]))

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([hue-5,100,100])
    upper_blue = np.array([hue+10,255,255])
    
    mask = cv2.inRange(img, lower_blue, upper_blue)

    ind = ind[mask > 0]

    if len(ind) > 10:
        oXR = int(round(st.median(ind[:, 0])))
        oYR = int(round(st.median(ind[:, 1])))

        oXR = int(oXR/sF)
        oYR = int(oYR/sF)

        img2 = cv2.rectangle(img2, (oYR + 50, oXR - 50), (oYR - 50, oXR + 50), (0,0,255), 4)
    return img2

    

# cv2.imshow("Light", findNDraw("/Users/yamanjandali/Desktop/Projects/colorFinder/redLED2.jpg"))
# cv2.waitKey(0)


cap = cv2.VideoCapture(0)

green = np.uint8([[[0,0,255]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)[0][0][0]
print(hsv_green)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    frame = findNDraw(frame, hsv_green)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

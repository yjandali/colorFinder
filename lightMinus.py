import cv2
import numpy as np
import statistics as st
import time


def indices(m,n):
    r0 = np.arange(m) # Or r0,r1 = np.ogrid[:m,:n], out[:,:,0] = r0
    r1 = np.arange(n)
    out = np.empty((m,n,2),dtype=int)
    out[:,:,0] = r0[:,None]
    out[:,:,1] = r1
    return out

def findNDraw(img2, imgBase, sF = 1, count = 0, color = "red"):
    # img = cv2.imread(link, 1)

    img = cv2.resize(img2, (0, 0), fx =sF, fy=sF)

    img3 = (img[:, :, 2] + img[:, :, 0])
    imgR = img[:, :, 2]

    shp = img.shape

    ind = np.array(indices(shp[0], shp[1]))

    # img = np.array(img[:, :, 0] + img[:, :, 1] + img[:, :, 2])

    ind = ind[(imgR > 254)]
    
    if len(ind) > 0:
        oXR = int(round(st.median(ind[:, 0])))
        oYR = int(round(st.median(ind[:, 1])))

        oXR = int(oXR/sF)
        oYR = int(oYR/sF)

        img2 = cv2.rectangle(img2, (oYR + 50, oXR - 50), (oYR - 50, oXR + 50), (0,0,255), 4)
        count += 1
        print(count)

    return img2, count

# cv2.imshow("Light", findNDraw("/Users/yamanjandali/Desktop/Projects/colorFinder/redLED2.jpg"))
# cv2.waitKey(0)


cap = cv2.VideoCapture(0)
count = 0
ret, imgBase = cap.read()


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    (frame, count) = findNDraw(frame, imgBase, 0.5, count)
    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

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

def findNDraw(img2, sF = 1, color = "red"):
    # img = cv2.imread(link, 1)
    img = cv2.resize(img2, (0, 0), fx =sF, fy=sF)

    shp = img.shape

    imgB = np.array(img[:, :, 1])
    imgR = np.array(img[:, :, 2])

    ind = ind2 = np.array(indices(shp[0], shp[1]))

    imgCR = np.array(img[:, :, 1] + img[:, :, 0])
    imgCB = np.array(img[:, :, 0] + img[:, :, 2])

    ind = ind[(imgR > 230) & (imgCR < 30)]

    if len(ind) > 10:
        oXR = int(round(st.median(ind[:, 0])))
        oYR = int(round(st.median(ind[:, 1])))

        oXR = int(oXR/sF)
        oYR = int(oYR/sF)

        img2 = cv2.rectangle(img2, (oYR + 50, oXR - 50), (oYR - 50, oXR + 50), (0,0,255), 4)
    else:
        oYR = -1    


    

    ind2 = ind2[(imgB > 230) & (imgCB < 30)]

    if len(ind2) != 0:
        oXB = int(round(st.median(ind2[:, 0])))
        oYB = int(round(st.median(ind2[:, 1])))

        oXB = int(oXB/sF)
        oYB = int(oYB/sF)

        img2 = cv2.rectangle(img2, (oYB + 50, oXB - 50), (oYB - 50, oXB + 50), (0,255,0), 4)
    else:
        oYB = -1

    return img2, oYR, oYB

# cv2.imshow("Light", findNDraw("/Users/yamanjandali/Desktop/Projects/colorFinder/redLED2.jpg"))
# cv2.waitKey(0)

temp = 100;
fD = False
cap = cv2.VideoCapture(0)
stepCount = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    
    frame, yR, yB = findNDraw(frame, sF = 0.3)
 
    # if y != -1:
    #     print (abs(temp - y))
    #     print(temp, y)
    #     temp = y
        
    if fD == False and yR != -1:
        fD = True
        stepCount+=1
        print("step ", stepCount, "!")


    elif fD == True and yR == -1 and yB != -1:
        fD = False
        stepCount+=1
        print("step ", stepCount,"!")


    # Display the resulting frame
    cv2.imshow('frame',frame)
    # cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

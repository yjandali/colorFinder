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

img = cv2.imread("C:\\Users\\Yaman\Desktop\\colorFinder\\RBLED1.jpg", 1)

#img = cv2.resize(img, (0, 0), fx =0.15, fy=0.15)
imgR = np.array(img[:, :, 2])
imgB = np.array(img[:, :, 0])

shp = imgR.shape
 
ind = ind2 = np.array(indices(shp[0], shp[1]))

imgCR = np.array(img[:, :, 1] + img[:, :, 0])
imgCB = np.array(img[:, :, 2] + img[:, :, 1])

ind = ind[(imgR > 200) & (imgCR < 30)]
ind2 = ind2[(imgB > 200) & (imgCB < 30)]

# cv2.imshow('Red Light', img)

# cv2.waitKey(0)

# cv2.imshow('Red Light', img2)

# cv2.waitKey(0)

# (x, y) = np.unravel_index(img2.argmax(), img2.shape)

# max = img2[x, y]

# vals = [np.anywhere((imgC < 250*3) && (imgR > 200))]




oXR = int(round(st.median(ind[:, 0])))
oYR = int(round(st.median(ind[:, 1])))

oXB = int(round(st.median(ind2[:, 0])))
oYB = int(round(st.median(ind2[:, 1])))

#print((vals[:, 1]).shape())

#(oX, oY) = np.unravel_index(np.argmax(b, axis=None), b.shape)  # returns a tuple

# for idy, row in enumerate(b):
#     for idx, el in enumerate(row):
#         if el == (b[oX, oY]):
#             x+=idx
#             y+=idy
#             counter+=1
# oX = int(x/counter)
# oY = int(y/counter)

#print(oX, oY)



# maxElem = max(imgArray)
# coords = np.where(imgArray>=maxElem-5)[0]

# x = sum([el[0] for el in coords])
# y = sum([el[1] for el in coords])

# print(x, y)

# oX = int(img.shape[0]/2)
# oY = int(img.shape[1]/2)

img = cv2.rectangle(img, (oYR + 50, oXR - 50), (oYR - 50, oXR + 50), (0,0,255), 4)

img = cv2.rectangle(img, (oYB + 50, oXB - 50), (oYB - 50, oXB + 50), (255,0,0), 4)

cv2.imshow('Red Light', img) 

cv2.waitKey(0)

# cv2.imwrite("C:\\Users\\Yaman\Desktop\\pyScripts\\panda2.jpg", img)


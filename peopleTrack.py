import numpy as np
import cv2

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


# def draw_detections(img, rects, thickness = 1):
#     for x, y, w, h in rects:
#         # the HOG detector returns slightly larger rectangles than the real objects.
#         # so we slightly shrink the rectangles to get a nicer output.
#         pad_w, pad_h = int(0.15*w), int(0.05*h)
#         cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
def draw_detections(img, rect, color = (0, 255, 0), thickness = 1):
    x, y, w, h = rect
    # the HOG detector returns slightly larger rectangles than the real objects.
    # so we slightly shrink the rectangles to get a nicer output.
    pad_w, pad_h = int(0.15*w), int(0.05*h)
    
    cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), color, thickness)
    return (int(((x+pad_w)+ (x+w-pad_w))/2), int(((y+pad_h)+y+h-pad_h)/2))

def draw_detections2(img, rect, posX, posY, color = (0, 0, 255), thickness = 1):
    x, y, w, h = rect
    marginX = 50
    marginY = 100
    # the HOG detector returns slightly larger rectangles than the real objects.
    # so we slightly shrink the rectangles to get a nicer output.
    pad_w, pad_h = int(0.15*w), int(0.05*h)
    retPosX, retPosY = (int(((x+pad_w)+ (x+w-pad_w))/2), int(((y+pad_h)+y+h-pad_h)/2))
    if ((abs(retPosX - posX) < marginX) and  (abs(retPosY - posY) < marginY)):
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), color, thickness)
        return (True, retPosX, retPosY)
    cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
    return (False, posX, posY)

if __name__ == '__main__':

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
    cap = cv2.VideoCapture("video.mp4")
    posX, posY = 0, 0
    margin = 20
    locked = False
    while(not locked):
        _,frame=cap.read()
        #frame = cv2.resize(frame, (0, 0), fx = .5, fy = .5)
        found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
        
    
        if(len(found)):
            for rect in found:
                x, y = draw_detections(frame, rect)
                cv2.imshow('feed',frame)
                if cv2.waitKey(0) & 0xFF == ord('y'):
                    frame = cv2.circle(frame, (x, y), 50, (255, 0, 0))
                    posX, posY = (x, y)
                    locked = True
                    print("locked on target")
                    cv2.imshow('feed',frame)
                


    while (locked):
        _,frame=cap.read()
        found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
        for rect in found:
            target, posX, posY = draw_detections2(frame, rect, posX, posY)
            cv2.imshow('feed',frame)
            if target == True:
                break
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
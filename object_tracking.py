import cv2

tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('rua.mp4')

ok, frame = video.read()

ok

bbox = cv2.selectROI(frame) #region of interest

#print(bbox)

ok = tracker.init(frame, bbox)

#print(ok)

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame)
    #print(bbox)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]

        cv2.rectangle(frame, (x,y),
                      (x+w,y+h),
                      color=(0,255,0),
                      thickness=2,
                      lineType=1)
    else:
        cv2.putText(frame,"Tracking failed",
                    (100,80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (255,0,0),2)
                    
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0XFF == 27:
        break
import cv2

video = cv2.VideoCapture(0)

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    success, img = video.read()

    faces = face.detectMultiScale(img, 1.3, 4)

    for (x, y, h, w) in faces:
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (99, 99), 0)
        img[y:y+h, x:x+w] = blur

    cv2.imshow("Blured Faces", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.realease()
cv2.destroyAllWindows()


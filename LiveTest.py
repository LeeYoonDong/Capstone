import cv2

# Load trained model
model = cv2.face.LBPHFaceRecognizer_create()
model.read('trained_model.yml')

# Load face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture video from default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # For each detected face, compare with the trained model
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        label, confidence = model.predict(roi_gray)
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # If confidence level is above 70%, label as a match
        if confidence < 70:
            cv2.putText(frame, 'TARGET', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        # Otherwise, label as not a match
        else:
            cv2.putText(frame, 'Nagetive', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

    # Show the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Check for 'q' key press to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()

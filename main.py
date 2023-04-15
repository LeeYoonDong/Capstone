# from keras.models import load_model  # TensorFlow is required for Keras to work
# import cv2  # Install opencv-python
# import numpy as np
#
# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)
#
# # Load the model
# model = load_model("keras_Model.h5", compile=False)
#
# # Load the labels
# class_names = open("labels.txt", "r").readlines()
#
# # CAMERA can be 0 or 1 based on default camera of your computer
# camera = cv2.VideoCapture(0)
#
# while True:
#     # Grab the webcamera's image.
#     ret, image = camera.read()
#
#     # Resize the raw image into (224-height,224-width) pixels
#     image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
#
#     # Show the image in a window
#     cv2.imshow("Webcam Image", image)
#
#     # Make the image a numpy array and reshape it to the models input shape.
#     image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
#
#     # Normalize the image array
#     image = (image / 127.5) - 1
#
#     # Predicts the model
#     prediction = model.predict(image)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     confidence_score = prediction[0][index]
#
#     # Print prediction and confidence score
#     print("Class:", class_name[2:], end="")
#     print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#
#     # Listen to the keyboard for presses.
#     keyboard_input = cv2.waitKey(1)
#
#     # 27 is the ASCII for the esc key on your keyboard.
#     if keyboard_input == 27:
#         break
#
# camera.release()
# cv2.destroyAllWindows()
#------1
# from keras.models import load_model  # TensorFlow is required for Keras to work
# import cv2  # Install opencv-python
# import numpy as np
#
# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)
#
# # Load the model
# model = load_model("keras_Model.h5", compile=False)
#
# # Load the labels
# class_names = open("labels.txt", "r").readlines()
#
# # Load the face cascade classifier
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#
# # CAMERA can be 0 or 1 based on default camera of your computer
# camera = cv2.VideoCapture(0)
#
# while True:
#     # Grab the webcamera's image.
#     ret, image = camera.read()
#
#     # Resize the raw image into (224-height,224-width) pixels
#     image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
#
#     # Show the image in a window
#     cv2.imshow("Webcam Image", image)
#
#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Detect faces in the grayscale image using the Haar Cascade Classifier
#     faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
#
#     # Draw a red square around each detected face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#
#         # Crop the face region from the original image and resize it to the model's input shape
#         face_region = cv2.resize(image[y:y+h, x:x+w], (224, 224), interpolation=cv2.INTER_AREA)
#
#         # Make the face region a numpy array and reshape it to the model's input shape
#         face_region = np.asarray(face_region, dtype=np.float32).reshape(1, 224, 224, 3)
#
#         # Normalize the face region array
#         face_region = (face_region / 127.5) - 1
#
#         # Predict the class of the face region using the model
#         prediction = model.predict(face_region)
#         index = np.argmax(prediction)
#         class_name = class_names[index]
#         confidence_score = prediction[0][index]
#
#         # Print prediction and confidence score
#         print("Class:", class_name[2:], end="")
#         print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#
#     # Listen to the keyboard for presses.
#     keyboard_input = cv2.waitKey(1)
#
#     # 27 is the ASCII for the esc key on your keyboard.
#     if keyboard_input == 27:
#         break
#
# camera.release()
# cv2.destroyAllWindows()

#-------2

# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model
#
# # Load the model and labels
# model = load_model('keras_model.h5')
# with open('labels.txt', 'r') as f:
#     labels = [line.strip() for line in f.readlines()]
#
# # Load the face detection classifier
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# # Start the video capture
# cap = cv2.VideoCapture(0)
#
# # Loop over frames from the video stream
# while True:
#     # Read the next frame from the video stream
#     ret, frame = cap.read()
#
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect faces in the grayscale frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Loop over the faces and draw boxes around them
#     for (x, y, w, h) in faces:
#         # Extract the face ROI
#         face_roi = gray[y:y+h, x:x+w]
#
#         # Resize and convert the face ROI to RGB format
#         face_roi = cv2.resize(face_roi, (224, 224))
#         face_roi = cv2.cvtColor(face_roi, cv2.COLOR_GRAY2RGB)
#
#         # Normalize the pixel values to the range [0, 1]
#         face_roi = face_roi.astype('float32') / 255.0
#
#         # Make a prediction on the face ROI
#         predictions = model.predict(np.expand_dims(face_roi, axis=0))
#
#         # Get the predicted label and confidence
#         label_index = np.argmax(predictions)
#         confidence = predictions[0][label_index]
#
#         # Draw a box around the face and label it with the predicted class
#         color = (0, 0, 255) if label_index == 0 else (0, 0, 255)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#         cv2.putText(frame, labels[label_index], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
#
#     # Display the resulting frame
#     cv2.imshow('Face Detection', frame)
#
#     # Exit the loop if the 'q' key is pressed
#     keyboard_input = cv2.waitKey(1)
#
#     if keyboard_input == 27:
#          break
#
# # Release the video capture and close the window
# cap.release()
# cv2.destroyAllWindows()
#
#-------
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the model and labels
model = load_model('keras_model.h5')
with open('labels.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start the video capture
cap = cv2.VideoCapture(0)

# Loop over frames from the video stream
while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the faces and draw boxes around them
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = gray[y:y+h, x:x+w]

        # Resize and convert the face ROI to RGB format
        face_roi = cv2.resize(face_roi, (224, 224))
        face_roi = cv2.cvtColor(face_roi, cv2.COLOR_GRAY2RGB)

        # Normalize the pixel values to the range [0, 1]
        face_roi = face_roi.astype('float32') / 255.0

        # Make a prediction on the face ROI
        predictions = model.predict(np.expand_dims(face_roi, axis=0))

        # Get the predicted label and confidence
        label_index = np.argmax(predictions)
        confidence = predictions[0][label_index]

        # Draw a box around the face and label it with the predicted class
        if confidence >= 0.5: # only draw box if confidence is greater than or equal to 70%
            color = (0, 255, 0) if label_index == 0 else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, labels[label_index], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Exit the loop if the 'q' key is pressed
    keyboard_input = cv2.waitKey(1)

    if keyboard_input == 27:
         break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()


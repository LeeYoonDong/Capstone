import os
import cv2
import numpy as np

# Define the path to the directory containing the face images
data_path = '/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/'

# Create a list of subdirectory names under the data path
subdirs = ['s1', 's2', 's3']

# Create a list to hold the labels for each face image
labels = []

# Create a list to hold the face data for each face image
faces_data = []

# Loop over each subdirectory
for i, subdir in enumerate(subdirs):
    subdir_path = os.path.join(data_path, subdir)
    # Loop over each image file in the subdirectory
    for filename in os.listdir(subdir_path):
        if filename.endswith('.jpg'):
            # Load the image file
            img_path = os.path.join(subdir_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            # Extract the label from the subdirectory name
            label = i + 1
            labels.append(label)
            # Add the face data to the list of faces data
            faces_data.append(img)
            print(f'Loaded image: {img_path}')

# Convert the label and face data lists to NumPy arrays
labels = np.array(labels)
faces_data = np.array(faces_data)

print('Starting model training...')
# Train the LBPHFaceRecognizer model using the face data and labels
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces_data, labels)
print('Model training completed successfully.')

# Save the trained model to a YAML file
model_filename = 'trained_model.yml'
recognizer.write(model_filename)
print(f'Trained model saved to file: {model_filename}')
recognizer.write('trained_model.yml')
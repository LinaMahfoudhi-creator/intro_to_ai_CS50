import cv2
import numpy as np
import tensorflow as tf

IMG_WIDTH = 30
IMG_HEIGHT = 30

def preprocess_image(image_path):
    """
    Prépare une image pour la prédiction.
    Redimensionne l'image et la normalise.
    """
    image = cv2.imread(image_path)
    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
    image = image / 255.0  # Normalisation
    return np.expand_dims(image, axis=0)  # Ajouter une dimension pour le batch

model = tf.keras.models.load_model("model.h5")


image_path = "path/to/image.jpg"


image = preprocess_image(image_path)

prediction = model.predict(image)
predicted_category = np.argmax(prediction)

print(f"Predicted category: {predicted_category}")
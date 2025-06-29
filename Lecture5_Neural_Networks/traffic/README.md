## Experimentation Process

In this project, we developed a convolutional neural network model to classify images of traffic signs into various categories. 
The goal was to design, train, and evaluate a model capable of effectively recognizing traffic signs from images.

### Steps Followed

1. **Data Preparation**: The data was loaded from a directory containing subfolders for each category. 
Each image was resized to a uniform size of 30x30 pixels to ensure consistency in the model input.
It was quite challenging considering it was my first time working with cv2 library in general.

2. **Data Splitting**: The dataset was divided into training and testing sets, 
with 40% of the data reserved for testing. Labels were converted into categorical format to match the model's output.

3. **Model Design**: A convolutional neural network was created with multiple convolutional layers, 
pooling layers, and fully connected layers. 
A dropout layer was added to reduce overfitting.

4. **Training**: The model was trained on the training set for 10 epochs using the Adam optimizer and a `categorical_crossentropy` loss function.

5. **Evaluation**: The model's performance was evaluated on the test set to measure its accuracy.


### Results and Observations

During experimentation, it was observed that the model's 
accuracy heavily depends on the quality of the data and the configuration 
of hyperparameters. Further improvements, such as data augmentation or adjustments to the network structure, could enhance performance. This project highlights the importance of data preprocessing and model design in image classification tasks.
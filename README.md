<<<<<<< HEAD
# Grade-It!

ESC 101 project undertaken during Fall Semester 2019 at IITK.

The aim was to create an application which is able to grade True/False questions in an answer script.

NodeJS was used to deal with the architecture and pipeline.

A Neural Network created in Tensforflow was used to recognize the characters.
=======
# AdvancedTrack
Project under Piyush Rai to auto grade answer scripts. Uses
 - **OpenCV** to preprocess images
 - **TensorFlow** to train the Deep Learning model
 - **MERN Stack** to act as the interface to upload answer sheets.
 
## Requirements
python>=2.7

npm>=6

## OpenCV
We first process the images before sending them into our ML model. We smoothen the image using *Gaussian Blur* to remove noise so that our *Sobel Operators* can detect edges well. Used *Canny Edge Detection* to identify the bounding boxes around the written text. 


![Pre-processing Images](./images/OpenCVT.png)
<div align="left"><em>Processed Handwritten T</em></div>

![Pre-processing Images](./images/OpenCVF.png)
<div align="left"><em>Processed Handwritten F</em></div>

## TensorFlow
We used *adam* as our optimizer to train our deep learning model. We used a sparse categorical cross-entropy loss function since our classes were mutually exclusive. We used the EMNIST Dataset to train our models, (including some local samples) to train our model and were able to achieve an accuracy of upto *98%*

![Tensor Flow Training](./images/TensorFlowTraining.png)

*Training of the model*

## HandleBars and Express
In order to serve as an interface to upload answer sheets as well as view marks, we created a website using nodejs. We used express to handle our routes for the server and Express Handlebars as a templating engine.

![Home Page](./images/HomePage.jpg)
<div align="left"><em>Home Page</em></div>

![Results Page](./images/ResultPage.png)
<div align="left"><em>Results Page</em></div>

>>>>>>> 82112ac663f19862b6bdb98a8ad957e49d6188ec

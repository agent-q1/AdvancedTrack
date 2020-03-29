import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
import numpy as np
import cv2
import os

# Function to make the image a square by adding padding
def makeSquare(not_square):
    BLACK = [0,0,0]
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    if(height == width):
        square = not_square
        return square
    else:
        doublesize = cv2.resize(not_square, (2*width,2*height), interpolation = cv2.INTER_CUBIC)
        height = height*2
        width = width*2
        if(height>width):
            pad = (height-width)/2
            doublesize_square = cv2.copyMakeBorder(doublesize,0,0,int(pad),int(pad),cv2.BORDER_CONSTANT, value=BLACK)
        else:
            pad = (width-height)/2
            doublesize_square=cv2.copyMakeBorder(doublesize,int(pad),int(pad),0,0,cv2.BORDER_CONSTANT, value=BLACK)
    return doublesize_square


train_labels = []
train_images=[]
test_labels = []
test_images=[]
for i in range(10,55):
    y = str(i)
    path = 'Sample030/img030-0'+y+'.png'
    img1 = cv2.imread(path ,0)
    blurred = cv2.GaussianBlur(img1, (5,5),0)
    edged = cv2.Canny(blurred,30,150)
    contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    (x,y,w,h)=cv2.boundingRect(cnt)
    roi = blurred[y:y+h,x:x+w]
    ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
    squared = makeSquare(roi)
    squared = cv2.resize(squared,(20,20))
    squared = cv2.copyMakeBorder(squared,4,4,4,4,cv2.BORDER_CONSTANT)
    squared = squared/255
    train_images.append(squared)
    train_labels.append(0)
for i in range(1,10):
    y = str(i)
    path = 'Sample030/img030-00'+y+'.png'
    img1 = cv2.imread(path ,0)
    blurred = cv2.GaussianBlur(img1, (5,5),0)
    edged = cv2.Canny(blurred,30,150)
    contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    (x,y,w,h)=cv2.boundingRect(cnt)
    roi = blurred[y:y+h,x:x+w]
    ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
    squared = makeSquare(roi)
    squared = cv2.resize(squared,(20,20))
    squared = cv2.copyMakeBorder(squared,4,4,4,4,cv2.BORDER_CONSTANT)
    squared = squared/255
    test_images.append(squared)
    test_labels.append(0)


for i in range(1,10):
    y = str(i)
    path = 'Sample016/img016-00'+y+'.png'
    img1 = cv2.imread(path ,0)
    blurred = cv2.GaussianBlur(img1, (5,5),0)
    edged = cv2.Canny(blurred,30,150)
    contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    (x,y,w,h)=cv2.boundingRect(cnt)
    roi = blurred[y:y+h,x:x+w]
    ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
    squared = makeSquare(roi)
    squared = cv2.resize(squared,(20,20))
    squared = cv2.copyMakeBorder(squared,4,4,4,4,cv2.BORDER_CONSTANT)
    squared = squared/255
    test_images.append(squared)
    test_labels.append(1)


for i in range(10,55):
    y = str(i)
    path = 'Sample016/img016-0'+y+'.png'
    img1 = cv2.imread(path ,0)
    blurred = cv2.GaussianBlur(img1, (5,5),0)
    edged = cv2.Canny(blurred,30,150)
    contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    (x,y,w,h)=cv2.boundingRect(cnt)
    roi = blurred[y:y+h,x:x+w]
    ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
    squared = makeSquare(roi)
    squared = cv2.resize(squared,(20,20))
    squared = cv2.copyMakeBorder(squared,4,4,4,4,cv2.BORDER_CONSTANT)
    squared = squared/255
    train_images.append(squared)
    train_labels.append(1)



a = np.array(train_images)




train_images = np.array(train_images)
train_labels = np.array(train_labels)

test_images = np.array(test_images)
test_labels = np.array(test_labels)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

# opening request1.txt to check which paper's template has been set
# and must be implemented
f = open("request1.txt","r")
reqcontents = f.read()
listreq = reqcontents.split(' ')

# storing Type of exam
typeExam = listreq[0]

# opening answer.txt to check the answers to the particular exam
answerF = open(typeExam+"answer.txt","r")
anscontent = answerF.read()
answers = []

# storing number of questions in Nquestions
Nquestions = len(anscontent)
# print(Nquestions)
f=open(typeExam+".txt", "r")
contents = f.read()
lista = []
lista = contents.split(' ')

listImg = []
outputFile = typeExam+'result.txt'
f = open(outputFile, "w")

# erasing the particular file
f.write("")

# opening the file in append mode to store the information of all students
f=open(outputFile,"a")


pathToImg = './'+typeExam


# running a loop through every image in the directory to run the classifier
# on and predict the scores
for filename in os.listdir(pathToImg):
    listImg=[]
    for y in range(Nquestions):

        # opening image
        img = cv2.imread("./"+typeExam+"/"+filename,0)   


        x1 = int(lista[y*4],10) - 74    
        y1 = int(lista[y*4+1],10)- 73      
        x2 = int(lista[y*4+2],10) -74
        y2 = int(lista[y*4+3],10) - 73


        # cropping the image based on coordinates received
        crop_img = img[y1:y2, x1:x2]
        img1 = cv2.imread(path ,0)
        img1 = crop_img
        cv2.imshow('images',img1)
        cv2.waitKey(0)

        # blurring the image to reduce noise and better feature extraction
        blurred = cv2.GaussianBlur(img1, (5,5),0)

        edged = cv2.Canny(blurred,30,150)

        # using contours to find the region of interest within the cropped image
        contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # checking if a contour was found
        if(len(contours)!=0):
            for i in range(len(contours)):
            
                cnt = contours[i]
                (x,y,w,h)=cv2.boundingRect(cnt)

                #choosing the right contour
                if((w<40)and(w>10)and(h<50)and(h>10)):
                    print(x,y,x+w,y+h)
                    break

            roi = blurred[y:y+h,x:x+w]
            #cv2.imshow('asda',roi)
            #cv2.waitKey(0)

            #  thresholding to create a binary image
            ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
        
        # Contour wasn't found
        else:
            roi = blurred
            ret,roi=cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)

        # Adding padding to make the image a square without changing 
        # aspect ratio
        squared = makeSquare(roi)
        squared = cv2.resize(squared,(20,20))

        # Adding boundary to mimic dataset
        squared = cv2.copyMakeBorder(squared,4,4,4,4,cv2.BORDER_CONSTANT)
        img1 = cv2.resize(squared,(512,512))
        cv2.imshow('images',img1)
        cv2.waitKey(0)
        squared=squared/255
        listImg.append(squared)
    a = np.array(listImg)


    predictions = model.predict(a)
    for i in range (Nquestions):
        
        if(anscontent[i]=='T'):
            
            answers.append(0)
        else:
            answers.append(1)

    countMarks = 0
    ansString = ""

    for i in range(Nquestions):
        pr = np.argmax(predictions[i]) 
        if(pr==0):
            ansString+="T"
        else:
            ansString+="F"
        if(pr==answers[i]):
            countMarks=countMarks+1
    ArrName = filename.split('.')
    BareFilename = ArrName[0]

    # Writing to a file that stores the final scores of all the roll numbers
    # along with their corresponding inputs
    f.write("%s %d %d %s %s\n"%(BareFilename,countMarks,Nquestions,ansString,anscontent))

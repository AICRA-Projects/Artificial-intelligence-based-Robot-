# Artificial-intelligence-based-Robot
Artificial intelligence (AI) and robotics are a powerful combination for automating tasks inside and outside of the factory setting. In recent years, AI has become an increasingly common presence in robotic solutions, introducing flexibility and learning capabilities in previously rigid applications.
This System design a mobile rescue Human detection robotic system based on Arduino to help the people on time which are trapped in natural calamity like disaster, earthquake, floods etc.It gives timely & accurately reflect dynamic situation of human in disaster region like in the underground regions to control room, so that rescue team of Experts & doctors can be sending to the victim’s location for primary treatment and can be sent to the safe place or hospital.
# how to operate 
## step 1:  Give Power to the robot by connecting White Usb Cable with USB connector of Power Bank 
## step 2:  Stand in front of the robot from 1 meter of distance
## step 3:  Robot will start moving once it Tracks human body 
## step 4:  Foward and Right or left will move by Real time Tracking of A.I Interface of Human body detection

# Hardware Components
* I shaped Motor 300rpm
* Arduino Uno 
* L298n Motor Driver 
* Arcylic chassis 
* Screw packet 
* Motor Clamp 
* Jumper Wires Male - female and Male -male 
* Lithium ION battery 12 v 
* Bread Board 
* Wheels 
* Nvidia JetSON Nano 
* USB Web Camera
* Red Button /switch 
* Lithium ION battery Holder 
* 12v connector Male and Female 
* Mobile POWER bank 
* USB Type C
* Samsung SD CARD 32gb 

# Methodology:
## Step 1:
Setup the hardware according to connection is required 
## Step 2 :
Boot Nvidia Jetson Nano 
## Step 3: Python Package  
A package is basically a directory with Python files and a file with the name init.py. This means that every directory inside of the Python path, which contains a file named init.py, will be treated as a package by Python. It's possible to put several modules into a Package.
## Step 4:
OpenCV installation

#### Opencv Install :
* sudo apt update
* sudo apt install python3-opencv
* sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    libtbb2 libtbb-dev libdc1394-22-dev \
* mkdir ~/opencv_build && cd ~/opencv_build git clone https://github.com/opencv/opencv.git && git clone https://github.com/opencv/opencv_contrib.git
* cd ~/opencv_build/opencv
mkdir build && cd build
* cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
* make -j8
* sudo make install
## Step 5 : Human body Detection 
## HOG – Histogram of Oriented Gradients
The histogram of oriented gradients is a feature descriptor algorithm used in computer vision and image processing. Its main purpose is object detection. The essential thought behind the HOG descriptor is that local object shape and appearance within an image can be described by the distribution of intensity gradients or edge directions.

This algorithm checks the surrounding pixels of every single pixel using the sliding window technique. The goal is to check how darker is the current pixel compared to the surrounding pixels and then it draws an arrow showing the direction of the image getting darker for every pixel. These arrows are called Gradients.

### Linear SVM -Linear Support Vector Machine
LSVM or Linear Support Vector Machine is a linear model for classification and regression problems. The idea behind SVM is that the algorithm creates a line or a hyperplane which separates the data into classes.
#### Explanation:

detectMultiScale() detects the objects from the image and returns their x and y coordinate, height, and width.
The winStride parameter indicates the step size in both the x and y location of the sliding window.
The padding parameter indicates the number of pixels in both the x and y direction in which the sliding window ROI is “padded” prior to HOG feature extraction.
The scale parameter controls the factor in which our image is resized at each layer of the image pyramid.

Setup your python code for human detection by using hog detection 

## Step 6 :
Setup your arduino code 
code : https://github.com/AICRA-Projects/Artificial-intelligence-based-Robot-/blob/main/data_lines_jetbot.ino

Digital Pins are used to interface with Jetson nano on the basis of digital input data reading 

## Conclusion :
Human following robot is very common in this technology era. Human following is a technique used by robot and autonomous vehicles to follow a human within a specific range. In this case, communication between the human and the robot is the most significant factor where sensor is needed to ensure its successfulness.
## Reference 
* https://developer.nvidia.com/embedded/jetson-nano-developer-kit
* https://debuggercafe.com/opencv-hog-hyperparameter-tuning-for-accurate-and-fast-person-detection/

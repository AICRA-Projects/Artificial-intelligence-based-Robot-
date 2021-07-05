# Artificial-intelligence-based-Robot
Artificial intelligence (AI) and robotics are a powerful combination for automating tasks inside and outside of the factory setting. In recent years, AI has become an increasingly common presence in robotic solutions, introducing flexibility and learning capabilities in previously rigid applications.
This System design a mobile rescue Human detection robotic system based on Arduino to help the people on time which are trapped in natural calamity like disaster, earthquake, floods etc.It gives timely & accurately reflect dynamic situation of human in disaster region like in the underground regions to control room, so that rescue team of Experts & doctors can be sending to the victim’s location for primary treatment and can be sent to the safe place or hospital.
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
Setup the hardware accordaing to connection is required 
## Step 2 :
Boot Nvidia Jetson Nano 
## Step 3:
OpenCV installation
#### Opencv Install :
* sudo apt update
* sudo apt install python3-opencv
* sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    libtbb2 libtbb-dev libdc1394-22-dev \
* mkdir ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
* cd ~/opencv_build/opencv
mkdir build && cd build
* cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..

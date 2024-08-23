Object Detection with Detectron2
Overview
This project demonstrates object detection using Detectron2, a state-of-the-art object detection library built by Facebook AI Research. It provides scripts for installing Detectron2, setting up a prediction model, and running object detection on images.

Installation
Clone the Repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone <repository-url>
Install Dependencies: Navigate to the project directory and run the installation script to install the required dependencies:

bash
Copy code
cd object-detection-detectron2
./installation.sh
Usage
Setting up the Prediction Model: Before running object detection, you need to set up the prediction model. Modify the prediction_model.py script to specify the path to your trained model .pth file.

Running Object Detection: Use the main.py script to run object detection on images. Provide the URL of the image you want to analyze as a command-line argument. For example:

bash
Copy code
python main.py <image-url>
If the image contains objects that meet the detection threshold, it will display the image with bounding boxes around the detected objects. Otherwise, it will indicate that the image is not verified.

File Structure
installation.sh: Bash script for installing dependencies.
prediction_model.py: Python script for setting up the prediction model.
main.py: Main Python script for running object detection.
run.sh: Bash script for executing the object detection script with an image URL.
Dependencies
PyYAML
Detectron2
PyTorch
TorchVision
OpenCV

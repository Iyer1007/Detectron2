#!/bin/bash

# Install PyYAML
python -m pip install pyyaml==5.1

# Clone the Detectron2 repository
git clone https://github.com/facebookresearch/detectron2

# Install Detectron2 dependencies
python -m pip install -e detectron2

# Install additional required packages
python -m pip install torch torchvision opencv-python-headless

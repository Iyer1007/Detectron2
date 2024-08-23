import sys
import cv2
import numpy as np
import requests
from skimage import transform
from PIL import Image
from google.colab.patches import cv2_imshow
import tempfile
from prediction_model import predictor

# Assuming predictor is defined and loaded elsewhere
def detect_objects(image_path):
    im = cv2.imread(image_path)
    outputs = predictor(im)
    return outputs

def check_scores(outputs, threshold=0.98):
    scores = outputs['instances'].scores
    return any(score > threshold for score in scores)

def get_max_score(outputs):
    if outputs['instances'].scores.numel() == 0:
        return 0
    return outputs['instances'].scores.max().item()

def image_rotation(img, i):
    if i == 1:
        # Rotate 90 degrees clockwise
        rotated_img = np.rot90(img, k=3)
    elif i == 2:
        # Rotate 180 degrees
        rotated_img = np.rot90(img, k=2)
    elif i == 3:
        # Rotate 270 degrees clockwise (or 90 degrees counterclockwise)
        rotated_img = np.rot90(img, k=1)
    else:
        rotated_img = img  # If i == 0, no rotation
    return rotated_img

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        img_data = response.content
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(img_data)
            temp_file_path = temp_file.name
        return temp_file_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None

def process_image(image_path):
    if image_path is None:
        return "Image not found"
    
    im = cv2.imread(image_path)
    if im is None:
        return "Image not found"

    best_score = 0
    best_output = None

    for i in range(4):  # Start with the original and rotate up to 3 times
        outputs = predictor(im)
        max_score = get_max_score(outputs)
        if max_score > best_score:
            best_score = max_score
            best_output = outputs

        if check_scores(outputs):
            #print(f"Acceptable scores found on rotation {i}")
            break
        else:
            #print(f"Scores not acceptable on rotation {i}, rotating image")
            im = image_rotation(im, i + 1)

    if best_score < 0.98:
        return "Image not verified"

    # Draw bounding boxes on the image
    boxes = best_output['instances'].pred_boxes.tensor.cpu().numpy()
    for box in boxes:
        start_point = (int(box[0]), int(box[1]))
        end_point = (int(box[2]), int(box[3]))
        color = (0, 255, 0)  # Green color for bounding box
        thickness = 2
        im = cv2.rectangle(im, start_point, end_point, color, thickness)

    # Display the image with bounding boxes
    cv2_imshow(im)
    return best_output

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_image.py <image_url>")
        sys.exit(1)
    
    image_url = sys.argv[1]
    image_path = download_image(image_url)
    best_output = process_image(image_path)

    # Do something with best_output
    if best_output == "Image not verified":
        print(best_output)
    else:
        print("Image verified and displayed with bounding boxes")

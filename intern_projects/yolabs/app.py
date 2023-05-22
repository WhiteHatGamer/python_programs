"""
This Program is to entry a person into a stall, when the id card/board allows or not
"""
import cv2
import pytesseract as tess
from string import punctuation

# Path to the Tesseract OCR executable (adjust this based on your system)
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define color ranges for green and red in HSV color space
green_lower = (40, 50, 50)
green_upper = (80, 255, 255)
red_lower = (0, 50, 50)
red_upper = (20, 255, 255)

# Capture an image from the camera
#_, frame = cv2.VideoCapture("https://192.168.0.100:4747/video")
img = cv2.imread('test1.png')

# Convert the captured image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to binary using adaptive thresholding
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Apply color thresholding to create a mask for green and red regions
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

green_mask = cv2.inRange(hsv_image, green_lower, green_upper)

red_mask = cv2.inRange(hsv_image, red_lower, red_upper)


# Apply the green mask to the binary image
green_result = cv2.bitwise_and(binary_image, binary_image, mask=green_mask)

# Perform Optical Character Recognition on the green result image
green_text = tess.image_to_string(green_result).lower()
print("Text = "+green_text)

# Formatting string for better Abstraction
for let in green_text:
    if let in [*punctuation]:
        green_text = green_text.replace(let,'')


# Check if "Allow" is present in the green text
if "allow" in green_text:
    if "dont" in green_text:
        print("Do not allow access")
        # Perform actions to deny access
    else:
        print("Allow access")
        # Perform actions to grant access
else:
    print("Do not allow access")
    # Perform actions to deny access

# Release the camera
cv2.waitKey(0)
cv2.destroyAllWindows()

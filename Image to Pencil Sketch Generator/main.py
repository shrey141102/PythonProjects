import cv2

image = cv2.imread("Image to Pencil Sketch Generator/image/dog.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Concatenate the original and pencil sketch horizontally
combined = cv2.hconcat([image, cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2BGR)])

# Display the combined image
cv2.imshow("Original vs Pencil Sketch", combined)
cv2.waitKey(0)

# Save the pencil sketch image
cv2.imwrite(
    "Image to Pencil Sketch Generator/image/pencil_sketch_output.jpg", pencil_sketch
)

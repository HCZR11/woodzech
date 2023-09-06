from PIL import Image

# Open the image
input_path = 'img/veioze/rz1.jpeg'  # Replace with your input image path
output_path = 'img/veioze/rz_new1q.jpg'  # Replace with your output image path
image = Image.open(input_path)

# Set the new size
new_size = (323, 518)  # Replace with the desired dimensions (width, height)

# Resize the image
resized_image = image.resize(new_size, Image.ANTIALIAS)

# Save the resized image
resized_image.save(output_path)

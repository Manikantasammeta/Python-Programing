import pandas as pd
import os
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO

# Load the Excel workbook
workbook_path = 'C:/Users/manik/Downloads/Book1.xlsx'
wb = load_workbook(workbook_path)
sheet = wb.active  # Access the active sheet

# Directory to save extracted images
image_dir = "extracted_images"
os.makedirs(image_dir, exist_ok=True)

# Extract images and map them to row numbers
image_map = {}
for image in sheet._images:  # Access embedded images
    row = image.anchor._from.row + 1  # Get the row where the image is located (1-based index)
    binary_data = image._data()  # Access raw binary data of the image

    # Convert binary data to an actual image
    try:
        img = Image.open(BytesIO(binary_data))
        image_path = os.path.join(image_dir, f"image_row_{row}.png")
        img.save(image_path)  # Save the image to a file
        image_map[row] = image_path  # Map the image path to the row
    except Exception as e:
        print(f"Failed to process image for row {row}: {e}")
        image_map[row] = 'default_image.jpg'  # Assign a default image path on failure

# Load the Excel data as a DataFrame
data = pd.read_excel(workbook_path)

# Add image paths to the DataFrame
data['image_path'] = data.index.map(lambda idx: image_map.get(idx + 1, 'default_image.jpg'))

# Process the data
for index, row in data.iterrows():
    student_name = row.get('Name', 'None')
    student_id = row.get('ID', 'None')
    student_image = row.get('image_path', 'default_image.jpg')  # Default image if missing

    # Check if the image exists
    if not os.path.exists(student_image):
        print(f"Image for {student_name} (ID: {student_id}) not found. Using default.")
        student_image = "default_image.jpg"  # Replace with a valid default image path
    else:
        print(f"Image for {student_name} (ID: {student_id}) found: {student_image}")

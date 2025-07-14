import requests
import base64

url = "http://localhost:8000/ocr"
image_path = "path/to/your/image.jpg"

with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {
    "image": encoded_string,
    "probability": False,
    "png_fix": False
}

response = requests.post(url, data=data)
print(response.json())
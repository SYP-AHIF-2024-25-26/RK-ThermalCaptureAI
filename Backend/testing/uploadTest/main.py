import requests

url = "http://localhost:5197/upload"  # Replace with your API URL
file_path = "images/cat.1.jpg"  # Replace with the path to your image

with open(file_path, 'rb') as f:
    print(f)
    files = {'file': (f.name, f, 'image/jpeg')}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.text)
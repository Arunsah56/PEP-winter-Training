import requests

url = "http://127.0.0.1:8000/api/create-student/"

data = {
    "name": "kalu",
    "age": 21,
    "course": "science"
}

response = requests.post(url, json=data)

print(response.json())
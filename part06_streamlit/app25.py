import requests

data = {
    "id":"admin",
    "password":"1234"
}

response = requests.post(
    "http://localhost:5083/api/login",
    json=data,
    verify=False
)

print(response.text)
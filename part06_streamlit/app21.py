import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.text)

data = response.json()

print(data)
print(data[0]["name"])  # 특정값 출력
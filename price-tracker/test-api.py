import requests

response = requests.get("https://api.github.com/users/amri-03")

print("Status Code: ", response.status_code)
print("Content Type: ", response.headers["Content-Type"])

data = response.json()

print("Username: ", data["login"])
print("Public Repos: ", data["public_repos"])
print("Account Created: ", data["created_at"])

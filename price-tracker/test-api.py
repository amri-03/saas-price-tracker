import requests

url = "https://api.github.com/users/amri-03"

# Requests data from the server using the request library's get method
response = requests.get(url)

print("Status Code: ", response.status_code)
print("Content Type: ", response.headers["Content-Type"])

# Converts the raw response into structured json file
data = response.json()

# Avoids error when the user does not exist
if response.status_code != 200:
    print(f"Failed to fetch data.")
else:
    print("Username: ", data["login"])
    print("Public Repos: ", data["public_repos"])
    print("Account Created: ", data["created_at"])
    print("Updated At: ", data["updated_at"])

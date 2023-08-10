import requests
import sys

def get_github_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print("Your GitHub user ID is:", user_id)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
import requests

url = "https://api.github.com/user/repos"
headers = {
    "Authorization": "Bearer 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",  # example header
    "Accept": "application/vnd.github+json"          # GitHub recommends this
}
response = requests.get(url, headers=headers)
jsonResponse = response.json()
# owner = jsonResponse(0).owner.login
owner = jsonResponse[0]
print(owner["owner"]["login"])


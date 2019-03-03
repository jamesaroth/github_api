import requests, json

root = "https://api.github.com/"
base = "https://api.github.com/users/"
base_user = "https://api.github.com/user/"
f = open("/Users/yellowheart/Desktop/.access/github_token.txt", 'r')
token = f.readline().strip()
username = f.readlines(1)
username = username[0].strip()
pwd = f.readlines(2)
pwd = pwd[0].strip()
headers = {"Authorization": "token " + token}

repo_list = requests.get(base + username + "/repos", auth=(username, token))
for repo in repo_list.json():
    print(repo.get('name'))

def create_repo(name):
    payload = {'name': name, 'description': 'created via API'}
    c = requests.post(base_user + "repos", headers=headers, data=json.dumps(payload))
    return c.json()

def delete_repo(name):
    d = requests.delete(root + "repos/" + username + "/" + name, auth=(username, token))
    return d
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
headers = {"Authorization": "token" + token}

repo_list = requests.get(base + username + "/repos", auth=(username, token))
for repo in repo_list.json():
    n = repo.get('name')
    des = repo.get('description')
    own = repo.get("owner")

def create_repo(name):
    payload = {'name': name, 'description': 'created via API'}
    c = requests.post(base_user + "repos", auth=(username, token), data=json.dumps(payload))
    return json.loads(c.content)

# create_repo("hihihi")

# DELETE /repos/:owner/:repo
# login = requests.delete('https://api.github.com/' + 'repos/' + user + '/' + repo, headers=headers)

def delete_repo(name):
    d = requests.delete(root + "repos/" + username + "/" + name, auth=(username, token))
    return d



# for repo in repo_list.json():
#     print(repo.get("name"))



# curl -H "Authorization: token e581df6fbee1a0a54e43a1af267578c80db80cda" https://api.github.com


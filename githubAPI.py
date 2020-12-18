from github import Github
import requests
from pprint import pprint

def getUserData(username):
	url = f"https://api.github.com/users/{username}"
	userData = requests.get(url).json()
	return userData

def getUserRepos(username):
	g = Github()
	user = g.get_user(username)	
	output = ""
	for repo in user.get_repos():
		output += (str(repo) + "\n")
	return output

username = input("Enter GitHub username: ")

pprint(getUserData(username)) 
print(getUserRepos(username))
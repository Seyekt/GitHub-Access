import requests
from pprint import pprint

def getUserData(username):
	url = f"https://api.github.com/users/{username}"
	userData = requests.get(url).json()
	return userData

username = input("Enter GitHub username: ")

pprint(getUserData(username)) 


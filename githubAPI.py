import requests

def getUserData(username):
	url = f"https://api.github.com/users/{username}"
	userData = requests.get(url).json()
	print(userData)

getUserData("Seyekt") 


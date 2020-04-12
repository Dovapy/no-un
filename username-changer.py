import requests
import json
import time


print("Welcome to my Username changer script.")
token = input("Enter you token : ")
pwd = input("Enter you password : ")
pseudo = input("Enter the pseudonym you want to put : ")
nombrei = 1

header = {"authorization": f'{token}', "Content-Type": 'application/json' }
url = 'https://discordapp.com/api/v6/users/@me'
payload = {"username": f"{pseudo} [{nombrei}]", "password": f'{pwd}' }




i = 0
while i < 200000:
    r = requests.patch(url, headers=header, data=json.dumps(payload))
    r.json()
    print("\n \nRequest response : \n")
    print(r.json())
    print("\n \n")
    print(f"Username changed to \"{pseudo} [{nombrei}]\" \n \n")
    time.sleep(900)
    i = i + 1
    nombrei = nombrei + 1

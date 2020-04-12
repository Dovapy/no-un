import requests
import json
import time


print("Welcome to my Username changer script.")
token = input("Enter you token : ")
pwd = input("Enter you password : ")
pseudo = input("Enter the pseudonym you want to put : ")






j = 0
i = 0
while i < 200000:
    header = {"authorization": f'{token}', "Content-Type": 'application/json' }
    url = 'https://discordapp.com/api/v6/users/@me'
    payload = {"username": f"{pseudo} [{j}]", "password": f'{pwd}' }
    r = requests.patch(url, headers=header, data=json.dumps(payload))
    r.json()
    print("\n \nRequest response : \n")
    print(r.json())
    print("\n \n")
    print(f"Username changed to \"{pseudo} [{j}]\" \n \n")
    i = i + 1
    j = j + 1
    time.sleep(900)
    

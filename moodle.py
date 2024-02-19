import requests
import urllib.parse as urlparse
from bs4 import BeautifulSoup

def user_info(cred_path):
    with open(cred_path, "r") as f:
        username=f.readline()
        password=f.readline()
        return {
            "username" : username.strip(), "password" : password
        }

def login():
    url="https://moodle2023.muroran-it.ac.jp/login/index.php"
    session=requests.Session()
    getedurl=session.get(url)
    soup=BeautifulSoup(getedurl.text, "html.parser")
    logintoken=soup.find(attrs={"name" : "logintoken"})["value"]
    #print(logintoken)
    data=user_info("cred_path.txt")
    data["logintoken"]=logintoken
    #print(data)
    headers={"content-type" : "application/x-www-form-urlencoded"}
    #headers=dict()
    res=session.post(url=url, data=data, headers=headers)
    

    after=session.get("https://moodle2023.muroran-it.ac.jp")
    #chk=BeautifulSoup(after.text, "html.parser")
    
    with open("tmp.txt", "wt") as file:
        file.write(after.text)

def grep(file):
    with open(file, "r") as f:
        content=f.read()
        if "ログアウト" in content:
            print("login is successed")
        


login()
grep("tmp.txt")








from bs4 import BeautifulSoup
import requests

def bring():
    url="https://moodle2023.muroran-it.ac.jp/login/index.php"
    get_res=requests.get(url)
    soup=BeautifulSoup(get_res.text, "html.parser")
    logintoken=soup.find(attrs={
        "name" : "logintoken"
    })["value"]
    print(logintoken)

    logintoken2=soup.find(attrs={
        "name" : "logintoken"
    })
    logintoken2=logintoken2.get("value")
    print(logintoken2)

    

bring()
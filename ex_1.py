from bs4 import BeautifulSoup
import requests

def bring():
    url="https://moodle2023.muroran-it.ac.jp/login/index.php"
    get_res=requests.get(url)
    soup=BeautifulSoup(get_res.text, "html.parser")
    string=soup.find("a", attrs={
        "href" : "https://moodle2023.muroran-it.ac.jp/login/forgot_password.php"
    })
    print(string.text)

bring()
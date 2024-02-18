from bs4 import BeautifulSoup
import requests

def bring():
    url="https://qiita.com/"
    get_res=requests.get(url)
    soup=BeautifulSoup(get_res.text, "html.parser")
    contents=soup.find_all("a", attrs={
        "class" : "style-1q3ho3v"
    })
    with open("output.txt", "wt") as f:
        for content in contents:
            url=content["href"]
            f.write(url+' ')
            title=content.text
            f.write(title+'\n')
        
bring()
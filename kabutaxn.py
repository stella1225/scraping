from bs4 import BeautifulSoup
import requests

def bring():
    url="https://kabutan.jp/themes/?theme="+input("調べたいテーマを入力してください： ")
    get_res=requests.get(url)
    soup=BeautifulSoup(get_res.text, "html.parser")
    check=soup.find("div", attrs={
        "class" : "e404"
    })
    
    if "お探しのページが見つかりません" in check.text:
        print("お探しのページが見つかりませんでした")
        return 
    lines=soup.find_all("td", attrs={
        "class" : "tal"
    })
    #print(lines)
    #print(type(lines))
    #print(lines.text) error
    
    with open("output.txt", "wt") as f:
        for line in lines:
            f.write(line.text+'\n')

bring()

    

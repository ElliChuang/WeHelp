# 『抓取』 PTT 電影版網頁原始碼(HTML)
import urllib.request as req
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

def get_data(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 『解析』原始碼，取得每篇文章的標題
    import bs4
    # 使用 BeautifulSoup 解析 HTML 格式文件
    web = bs4.BeautifulSoup(data, "html.parser") 
    titles = web.find_all("div", class_= "title")
    # 分類並串接
    title_1, title_2, title_3 =[], [], []
    for title in titles:
        if title.a == None:
            continue
        elif "[好雷]" in title.a.string :  # a 指 <a>
            title_1.append(title.a.string)
        elif "[普雷]" in title.a.string:
            title_2.append(title.a.string)
        elif "[負雷]" in title.a.string:
            title_3.append(title.a.string)
    # 寫到 txt
    with open("movie_1.txt", "a", encoding="utf-8") as file:
        for title in title_1:
            file.write(title + "\n")
    with open("movie_2.txt", "a", encoding="utf-8") as file:
        for title in title_2:
            file.write(title + "\n")
    with open("movie_3.txt", "a", encoding="utf-8") as file:
        for title in title_3:
            file.write(title + "\n")
    # 抓取上頁的連結
    next_link = web.find("a", string = "‹ 上頁") 
    return next_link["href"] # []內部放要找的“屬性”

page_url = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 10:
    page_url = "https://www.ptt.cc" + get_data(page_url)
    count += 1 

with open("movie_1.txt", "r", encoding="utf-8") as file:
    data_1 = file.read()
with open("movie_2.txt", "r", encoding="utf-8") as file:
    data_2 = file.read()
with open("movie_3.txt", "r", encoding="utf-8") as file:
    data_3 = file.read()
data = data_1 + data_2 + data_3
with open("movie_ver1.txt", "w", encoding="utf-8") as file:
    file.write(data)


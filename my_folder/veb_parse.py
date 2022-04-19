import requests
from bs4 import BeautifulSoup
import webbrowser
import os

url = 'https://www.postimees.ee/rss'
xml_data = requests.get(url).content
soup = BeautifulSoup(xml_data,"xml")
items = soup.find_all('item')
counts = 0
save_items = []
for i in items:
    item = []
    title = i.find("title").text
    description = i.find("description").text
    author = i.find("author").text
    enclosure  = i.find("enclosure")['url']
    item.append(title)
    item.append(description)
    item.append(author)
    item.append(enclosure)
    save_items.append(item)
    counts = counts+1
    if counts == 5:
        counts = 0
        break
with open ("index.html","w",encoding="utf8") as q:
    article1 = ""
    article2 = ""
    article3 = ""
    article4 = ""
    article5 = ""
    for w in range(5):
        item = save_items[w]
        article = f"""<article>
                        <h2>{item[0]}</h2>
                        <img src='{item[3]}'>
                        <p>{item[1]}</p>
                        <p>{item[2]}</p>
                    </article>"""
        if w == 0:
            article1 = article
        if w == 1:
            article2 = article
        if w == 2:
            article3 = article
        if w == 3:
            article4 = article
        if w == 4:
            article5 = article

    main = f""""<!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        <script src='main.js'></script>
    </head>
    <body>
        <div class="wrapper">
            {article1}
            {article2}
            {article3}
            {article4}
            {article5}
        </div>
    </body>
    </html>"""
    q.write(f"{main}")
filename = 'file:///'+os.getcwd()+'/' + 'index.html'
webbrowser.open_new_tab(filename)
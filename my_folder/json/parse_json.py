import json
import webbrowser
import os
main = """"<!DOCTYPE html>
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
        <div class="wrapper">"""
with open("my_folder/json/movies.json","r") as q:
    file = json.load(q)
with open ("index.html","w",encoding="utf8") as q:
    for i in file:
        article = f"""<article>
                            <h2>{i['Title']}</h2>
                            <img src='{i['Poster']}'>
                            <p>{i['Year']}</p>
                            <p>{i['Plot']}</p>
                        </article>"""
        main = main+article+"<br>"
    main = main+"""</div>
    </body>
    </html>"""
    q.write(f"{main}")
filename = 'file:///'+os.getcwd()+'/' + 'index.html'
webbrowser.open_new_tab(filename)



main = """"<!DOCTYPE html>
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
        <div class="wrapper">"""
with open("my_folder/json/pizza.json","r") as q:
    file = json.load(q)
with open ("pizza.html","w",encoding="utf8") as pizza:
    for i in file:
        article = f"""<article>
                            <h2>{i['name']}</h2>
                            <img src='{i['image']}' style="width:50%;">"""
        p = """<p>"""
        for q in i["dough"]:
            p = p+q["name"]+q["count"]+q["unit"]+", "
        p = p+"</p>"
        article = article + p
        p = """<p>"""
        for w in i["filling"]:
            p = p+w["name"]+w["count"]+w["unit"]+", "
        p = p+"</p>"
        article = article+"</article>"
        main = main+article+"<br>"
    main = main+"""</div>
    </body>
    </html>"""
    pizza.write(f"{main}")
filename = 'file:///'+os.getcwd()+'/' + 'pizza.html'
webbrowser.open_new_tab(filename)
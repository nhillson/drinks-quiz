import json, os
cards = json.load(open("src/cards.json"))
slim = [{k: c[k] for k in ("id","name","cat","sec","note","say")} for c in cards]
imgs = json.load(open("imgs.json")) if os.path.exists("imgs.json") else {}
t = open("src/template.html").read().replace("/*CARDS*/[]", json.dumps(slim)).replace("/*IMGS*/{}", json.dumps(imgs))
open("index.html","w").write(t); print(len(t)//1024, "KB")

with open("data/articles.bdf", 'r') as fichier_articles:
    articles = fichier_articles.read(-1).splitlines(False)

with open("data/clients.bdf", 'r') as fichier_clients:
    clients = fichier_clients.read(-1).splitlines(False)

articles.sort()
clients.sort()

article = ["---"]
prix = [0]
qtte = [0]

nom = []
tel = []
mail = []

for i in articles:
    if articles.count(i) > 1:
        articles.remove(i)
for i in articles:
    article.append(i.split(":")[0])
    prix.append(i.split(":")[1])
    qtte.append(i.split(":")[2])


for i in clients:
    if clients.count(i) > 1 or i.split("/")[0] == "":
        clients.remove(i)
for i in clients:
    nom.append(i.split("/")[0])
    tel.append(i.split("/")[1])
    mail.append(i.split("/")[2])


list_article = article
list_prix = prix
qtte_article = qtte

list_nom = nom
list_tel = tel
list_email = mail

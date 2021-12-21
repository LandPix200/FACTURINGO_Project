text = "" \
       "Salut les gars" \
       "\n[com]\n" \
       "ceci est un commentaire" \
       "nestpa\n" \
       "ne veenez pas mal" \
       "\n[/com]\n" \
       "commentaire fini"


def get_string_into(liste, debut, fin):
    texte = ""
    index_debut = 0
    index_fin = 0

    for i in range(0, len(liste.splitlines(False))):
        if liste.splitlines(False)[i] == debut:
            index_debut = i
        if liste.splitlines(False)[i] == fin:
            index_fin = i

    for i in range(0, len(liste.splitlines(False))):
        if (i > index_debut) and (i < index_fin):
            texte += (liste.splitlines(False)[i])

    return texte








import csv
import os


# Objectif : couper un fichier CSV en plusieurs morceaux en fonction du contenu
# de la première cellule de la ligne : si celle-ci contient tel contenu défini à l'avance,
# alors on ouvre un nouveau fichier où cette cellule devient la dernière ligne,
# et ainsi de suite quand on tombe sur une nouvelle cellule visée.


def write_output_file(file, cell):
    """Permet l'écriture d'un nouveau fichier (argument "file") jusqu'à une cellule
    donnée (argument "cell"). Les titres sont repris dans chaque nouveau fichier"""
    with open(file, 'w', encoding="utf-8", newline ='') as output_file :
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(headers)
        for row in reader:
            # Si je tombe sur la cellule demandée, je l'écris dans le fichier
            # et je stoppe la boucle
            if row[0] == cell:
                writer.writerow(row)
                break
            writer.writerow(row)


# Je définis le fichier source
source = input("Entrer le chemin et le nom complet du fichier à découper.\n")

# Je définis le nom commun de chaque fichier cible - ici, ce sera
# le nom du fichier source avec ajout de "1", "2", "3", etc.
split_file_prefix = input("Entrer le nom souhaité du fichier de sortie.\n")

# Je définis le contenu souhaité des cellules du fichier source
# qui vont enclencher la création et le remplissage de chaque nouveau fichier
# quand writer va arriver dessus
# création de la liste
cells = []
# entrée des données
print("Entrer le nom de chaque cellule qui sera en dernière ligne de chaque nouveau fichier. STOP pour arrêter.")

# Boucle while pour remplir la liste
i = 0
while 1:
    answer = input()
    # si j'écris "STOP", la list est arrêtée
    if answer == "STOP":
        break
    else:
        cells.append(answer)
print(f"les cellules concernées sont :\n{cells}. Un total de {len(cells)} nouveaux fichiers sera créé.")

# Je définis la liste des fichiers de sortie à partir de la liste des cellules
# "i" est l'indice de chaque fichier. Initialisé à 0, il prend 1 au début de chaque
# nouvelle itération.
output_list = []
i = 0
for cell in cells:
    i += 1
    output_list.append(f"{split_file_prefix}_{i}.csv")
print(output_list)

# J'ouvre le fichier source en lecture, encodage UTF-8
with open(source, 'r', encoding="utf-8") as input_file:
    reader = csv.reader(input_file, delimiter = ";")
    # Permet d'écrire le header dans chaque nouveau fichier
    headers = next(reader)
    i = 0
    # Je fais une boucle while sur les données de output_list et de cells
    # pour créer chaque fichier.
    while i < len(cells):
        write_output_file(output_list[i], cells[i])
        i += 1

# Inutile de fermer les fichiers d'entrée et sortie car j'ai utilisé with
print(f"fin du script. Les fichiers créés sont dans {os.getcwd()}")

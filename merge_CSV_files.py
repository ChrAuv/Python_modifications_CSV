import csv
import os
from pathlib import Path

# Posera souci si dans le fichier original les champs texte sont formatés entre guillemets
# Comment imposer un ordre dans la boucle ?
# Comment effacer la première ligne à partir du deuxième fichier traité ?
# Et si je veux le formatage entre guillemets ? Essayer avec csv.quotechar

with open('synthese.csv', 'w', encoding="utf-8", newline="") as output_file:
    writer = csv.writer(output_file, delimiter=';')
    # Les fichiers source doivent se trouver dans un répertoire "CSV"
    csv_directory = './CSV'
    csv_files_list = list(map(str,Path(csv_directory).glob('**/*.csv')))
    for file_name in csv_files_list:
        print(file_name)
        # Ici, écrire le fichier en mode texte ("t" ou "rt") et non en mode bytes ("rb")
        with open(file_name, 'rt', encoding="utf-8") as input_file:
            for row in csv.reader(input_file, delimiter=';'):
                writer.writerow(row)
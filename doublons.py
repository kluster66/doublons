import os
import argparse
import filecmp
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, help='to define')
args = parser.parse_args()
dir_path = args.dir

# Liste pour stocker les fichiers en double
duplicates = []

# Parcours récursif du répertoire
for root, dirs, files in os.walk(dir_path):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Comparaison de chaque fichier avec les autres fichiers
        for other_file_path in duplicates:
            if filecmp.cmp(file_path, other_file_path):

                # Calcul du hash des fichiers en double uniquement
                if os.path.getsize(file_path) == os.path.getsize(other_file_path):
                    hasher = hashlib.md5()
                    with open(file_path, 'rb') as f:
                        buf = f.read()
                        hasher.update(buf)
                    file_hash = hasher.hexdigest()

                    other_hasher = hashlib.md5()
                    with open(other_file_path, 'rb') as f:
                        buf = f.read()
                        other_hasher.update(buf)
                    other_file_hash = other_hasher.hexdigest()

                    if file_hash == other_file_hash:
                        print("Hashes identiques pour les fichiers: ")
                        print(file_path)
                        print(other_file_path)
                        print(file_hash, " = ", other_file_hash)
                        print(" ")
                break
        
        # Ajout du fichier à la liste des fichiers en double
        duplicates.append(file_path)

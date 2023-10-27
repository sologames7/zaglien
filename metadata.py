import os
import json
from decouple import config


# Chemin vers le dossier "generation-images" et "metadata"
generation_images_path = './generation-images/generation'
metadata_path = './metadata'

# Variable d'environnement "baseUri" from .env
base_uri = config('baseUri')

# Parcourez les fichiers du dossier "generation-images"
for filename in os.listdir(generation_images_path):
    if filename.endswith('.png'):
        # Construisez le chemin complet du fichier
        file_path = os.path.join(generation_images_path, filename)
        
        # image_id (bewteen # and .png)
        image_id = filename.split('#')[1].split('.')[0]
        # Construisez le nom de l'image
        image_name = filename.replace('#', '%23')
        
        # Créez le contenu JSON pour le fichier
        metadata = {
            "name": filename,
            "description": "Image générée avec un algorithme de superposition d'images originales.",
            "image": f"{base_uri}/{image_name}"
        }
        
        # Construisez le chemin complet du fichier JSON de métadonnées
        metadata_file_path = os.path.join(metadata_path, f"{image_id}.json")
        
        # Écrivez les métadonnées JSON dans le fichier
        with open(metadata_file_path, 'w') as json_file:
            json.dump(metadata, json_file, indent=2)

print("Métadonnées générées avec succès.")

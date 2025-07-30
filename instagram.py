import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def get_instagram_profile_pic(username):
    try:
        # URL del perfil de Instagram
        url = f"https://www.instagram.com/{username}/"
        
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()
        
        # Parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar la etiqueta meta que contiene la URL de la foto de perfil
        meta_tag = soup.find("meta", property="og:image")
        
        if meta_tag:
            profile_pic_url = meta_tag["content"]
            
            # Descargar la imagen
            file_name = f"{username}_profile_pic.jpg"
            urllib.request.urlretrieve(profile_pic_url, file_name)
            
            print(f"Foto de perfil descargada como {file_name}")
            return file_name
        else:
            print("No se pudo encontrar la foto de perfil.")
            return None
            
    except requests.exceptions.HTTPError as err:
        print(f"Error al acceder al perfil: {err}")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

if __name__ == "__main__":
    username = input("Ingresa el nombre de usuario de Instagram: ").strip()
    if username:
        get_instagram_profile_pic(username)
    else:
        print("Debes ingresar un nombre de usuario.")
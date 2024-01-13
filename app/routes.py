from flask import render_template, request, jsonify
from app import app  # Importa la instancia de la aplicación Flask
from app import pares, reflections  # Importa las variables 'pares' y 'reflections' desde __init__.py
from nltk.chat.util import Chat
import requests

# Definir las rutas
@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     user_message = request.args.get("msg")
#     chat = Chat(pares, reflections)
#     bot_response = chat.respond(user_message)
#     return jsonify({"response": bot_response})

@app.route("/get")
def get_bot_response():
    user_message = request.args.get("msg")
    chat = Chat(pares, reflections)
    bot_response = chat.respond(user_message)

    # Si el usuario ingresa "2", llamar al API y actualizar la respuesta del chatbot
    if user_message == "2":
        response = requests.get("https://dockermicroservicio.azurewebsites.net/productos")
        
        if response.status_code == 200:
            data = response.json()
            # Procesa la información según tus necesidades
            # Por ejemplo, puedes actualizar bot_response con los nombres de los productos
            product_names = [producto['nombre'] for producto in data]
            bot_response = f"Lista de productos:\n{', '.join(product_names)}"
        # Si el usuario ingresa "5", llamar al API de clientes y actualizar la respuesta del chatbot
    if user_message == "5":
        response = requests.get("https://dockermicroservicio.azurewebsites.net/clientes")
        
        if response.status_code == 200:
            data = response.json()
            # Procesa la información según tus necesidades
            # Por ejemplo, puedes actualizar bot_response con la lista de clientes y sus imágenes
            client_info = []
            for cliente in data:
                nombre = cliente['nombre']
                imagen = cliente['enlaceImagen']
                client_info.append(f"{nombre}: {imagen}")
            
            bot_response = f"Lista de clientes y sus imágenes:\n{', '.join(client_info)}"
            
    return jsonify({"response": bot_response})
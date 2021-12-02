from flask import Flask, jsonify , request

app = Flask(__name__)

lista_contatos = []

@app.route("/olamundo", methods= ["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201

@app.route("/contatos", methods = ["GET", "POST","PUT", "UPDATE"])
def contatos():
    if request.method == "GET":
        return jsonify(lista_contatos), 200
    elif request.method == "POST":
        contato = request.json
        lista_contatos.append(contato)
        return "", 200

@app.route("/contatos/<int:id_contato>", methods=["GET", "PUT", "DELETE"])
def contato(id_contato):
    if request.method == 'GET':
        try:
            info_contato = lista_contatos[id_contato]
            return jsonify(info_contato), 200
        except:
            return "", 404

app.run(port=8080)
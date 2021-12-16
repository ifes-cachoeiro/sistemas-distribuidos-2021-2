from flask import Flask, jsonify, request
from db import session, Cliente
from db import Produto, Carrinho, Venda

app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201


@app.route("/cliente", methods=["GET", "POST"])
@app.route("/cliente/<int:id_cliente>", methods=["GET", "PUT", "DELETE"])
def clientes(id_cliente=None):
    if request.method == "GET":
        if id_cliente:
            try:
                cliente = (
                    session.query(Cliente)
                    .filter(Cliente.id == id_cliente)
                    .one()
                )
                return (
                    jsonify({"id": cliente.id, "nome": cliente.nome}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_clientes = []
            clientes = session.query(Cliente).all()
            for c in clientes:
                lista_clientes.append({"id": c.id, "nome": c.nome})
            return jsonify(lista_clientes), 200
    elif request.method == "POST":
        cliente = request.json
        session.add(
            Cliente(nome=cliente["nome"], endereco=cliente["endereco"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        cliente = request.json
        session.query(Cliente).filter(Cliente.id == id_cliente).update(
            {"nome": cliente["nome"], "endereco": cliente["endereco"]}
        )
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Cliente).filter(
            Cliente.id == id_cliente
        ).delete()
        session.commit()
        return "", 200


app.run(host="0.0.0.0", port=8080)

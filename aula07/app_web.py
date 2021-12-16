from flask import Flask, jsonify, request
from db import session, Cliente
from db import Produto, Carrinho, Venda

app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201


@app.route("/cliente", methods=["GET", "POST", "PUT", "DELETE"])
def clientes():
    if request.method == "GET":
        lista_clientes = []
        # session.query(Cliente)
        # .filter(Cliente.id == 1)
        # .delete()
        clientes = session.query(Cliente).all()
        for c in clientes:
            lista_clientes.append(
                {
                    "id": c.id,
                    "nome": c.nome
                }
            )
        return jsonify(lista_clientes), 200
    elif request.method == "POST":
        cliente = request.json
        session.add(
            Cliente(
                nome=cliente["nome"],
                endereco=cliente['endereco']
            )
        )
        session.commit()
        return "", 200


@app.route("/cliente/<int:id_cliente>", methods=["GET", "PUT", "DELETE"])
def cliente(id_cliente):
    if request.method == "GET":
        try:
            cliente = (
                session.query(Cliente)
                .filter(Cliente.id_cliente == id_cliente)
                .one()
            )
            return (
                jsonify(
                    {"id_cliente": cliente.id_cliente, "nome": cliente.nome}
                ),
                200,
            )
        except Exception as ex:
            return "", 404
    elif request.method == "DELETE":
        try:
            session.query(Cliente).filter(
                Cliente.id_cliente == id_cliente
            ).delete()
        except Exception as ex:
            return "", 404


app.run(
    host="0.0.0.0",
    port=8080
)

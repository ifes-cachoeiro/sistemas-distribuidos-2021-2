from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v1/info', methods=['GET'])
def get_info():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return jsonify({'message': "Ola Mundo"})
    else:
        pass
    return jsonify({'message': "ola mundo"})

@app.route('/inicio', methods=['GET'])
def inicio():
    return '<h1> OLA MUNDO </h1>'


@app.route('/v1/contatos/<int:id_contato>', methods=['GET'])
def get_contatos(id_contato):
    if id_contato == 1000:
        return jsonify({'error': 'not found'}), 404
    else:
        return jsonify({'id_contato': id_contato}), 200

app.run(
    host='0.0.0.0',
    port=8080,
    debug=False)

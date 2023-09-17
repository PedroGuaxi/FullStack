from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)

# Esse arquivo é o CONTROLLER

# /pessoas, com GET, para pegar a lista de todas as pessoas


@app.route("/pessoas", methods=["GET"])
def pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)

# /pessoas, com POST, receber um dicionário de uma pessoa e colocar na lista


@app.route("/pessoas", methods=["POST"])
def add_pessoa():
    # receber um dicionário através do flask?
    # O usuário me mandou alguma coisa, eu acho que foi um json
    # quero que voce transforme num dicionário pra mim
    dic_usuario_enviou = request.json
    i.adiciona_pessoa(dic_usuario_enviou)
    return jsonify({"status": "ok"})


# /pessoas/id_pessoa, com GET, para localizar no dicionario da pessoa pelo id
@app.route("/pessoas/id_pessoa", methods=["GET"])
def search_pessoa():
    dic_usuario_enviou = request.json
    i.localiza_pessoa(dic_usuario_enviou)
    return jsonify({"status": "ok"})

# /pessoas/interesse, com POST, **aqui não tem corpo de requisição
# adiciona_interesse (id_interessado, id_alvo_de_interesse):


@app.route("/pessoas/interesse/", methods=["POST"])
def add_interest_pessoa():
    i.adiciona_interesse(id_interessado, id_alvo_de_interesse)
    return jsonify({"status": "ok"})

# /pessoas/interesse, com GET,
# consulta_interesses(id_interessado):


@app.route("/pessoas/interesse", methods=["GET"])
def search_interest_pessoa():
    i.consulta_interesses(id_interessado)
    return jsonify({"status": "ok"})

# /pessoas/interesse, com DELETE,
# remove_interesse(id_interessado, id_alvo_de_interesse)


@app.route("/pessoas/interesse", methods=["DELETE"])
def delete_interest_pessoa():
    i.remove_interesse(id_interessado, id_alvo_de_interesse)
    return jsonify({"status": "ok"})

# /pessoas/matches, com GET,
# lista_matches(id_pessoa):


@app.route("/pessoas/matches", methods=["GET"])
def search_interest_pessoa():
    i.lista_matches(id_pessoa)
    return jsonify({"status": "ok"})
# /reseta, com POST, para esvaziar a lista de pessoas


@app.route("/reseta", methods=["POST"])
def reseta():
    i.reseta()
    return jsonify({"status": "ok"})


if __name__ == '__main__':  # rodar o servidor
    app.run(host='localhost', port=5002, debug=True)

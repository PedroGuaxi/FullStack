from flask import Flask, jsonify, request 
import estrutura_interesses as i

app = Flask(__name__)              
     
#Esse arquivo é o CONTROLLER                              

# /aluno, com GET, para pegar a lista de todas os aluno
@app.route("/alunos", methods=["GET"])
def alunos():
    lista = i.todos()
    return jsonify(lista)

# /alunos, com POST, receber um dicionário de uma aluno e colocar na lista
@app.route("/alunos", methods=["POST"])
def add_aluno():
    #receber um dicionário através do flask?
    # O usuário me mandou alguma coisa, eu acho que foi um json
    # quero que voce transforme num dicionário pra mim
    dic_usuario_enviou = request.json
    i.adiciona_aluno(dic_usuario_enviou)
    return jsonify({"status":"ok"})


# /alunos/id_aluno, com GET, para localizar no dicionario da aluno pelo id
@app.route("/alunos/<int:id_aluno>", methods=["GET"])
def search_aluno(id_aluno):
    return i.localiza_aluno(id_aluno)
# /alunos/interesse, com DELETE,  
# remove_interesse(id_interessado, id_alvo_de_interesse)
@app.route("/alunos/delete/int:id_aluno>", methods=["DELETE"])
def delete_aluno(id_aluno):
    i.remove_aluno(id_aluno)
    return jsonify({"status": "ok"})

# /alunos/id_aluno, com GET, para localizar no dicionario da aluno pelo id
@app.route("/alunos/atualiza/<int:id_aluno>", methods=["PUT"])
def atualiza_aluno(id_aluno):
    dic_campo = request.json
    i.atualiza_aluno(id_aluno,dic_campo)
    return jsonify({"status": "ok"})

    
if __name__ == '__main__':         #rodar o servidor
   app.run(host = 'localhost', port = 5002, debug = True)

#esse arquivo é o MODEL

database = {}

class NotFoundError(Exception):
    pass
class IncompatibleError (Exception):
    pass


database['alunos'] = [
    {"id": 1, "nome": "Marcos","email": "marcos@gmail.com","user_type_Id":0,"password": "Banana@2324_m","isActive":1,"CPF_CNPJ":"400.289.220-02","phone":"40028922"}, 
]



def todos():
    return database['alunos']


def localiza_aluno(id_aluno):
    for i in database["alunos"]:
        if id_aluno == i['id']:
            return i
    raise NotFoundError


def adiciona_aluno(dic_aluno): #{'nome':'','id':}
    if dic_aluno not in database['alunos']:
        database["alunos"].append(dic_aluno)

def remove_aluno(id_aluno):

    localiza_aluno(id_aluno)
    for i in database['alunos']['id']:
        if id_aluno == i:            
            database['alunos'].remove()


def atualiza_aluno(id_aluno,dic_campo): #{'id':'0','dic_campo': 'novodado'}
    localiza_aluno(id_aluno)
    valor_campo= dic_campo['nome']
    chave_campo=""
    for chave in dic_campo.keys():
        chave_campo = chave
    for i in database['alunos']:
        if id_aluno == i:
            if chave_campo in database['alunos']:
                database['alunos']['nome'] = valor_campo
    print(database["alunos"])

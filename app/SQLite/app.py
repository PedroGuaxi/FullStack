import database, json
from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__,template_folder='../template', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/painel_admin', methods=['POST'] )
def painel_admin():
    user = ""
    users = database.show_all()
    name = request.form['name']
    password = request.form['password']
    for item in users:
        if item[1] == name and item[4] == password:
            user = open("user.txt", "w")
            user.write(str(item[0]))
            user.close()
            return render_template('painel.html')
        else:
            return render_template('index.html')


        
@app.route('/painel_users', methods=['GET'] )
def painel_users():
    # users = database.show_all()
    # name = request.form['name']
    # password = request.form['password']
    # for item in users:
    #     if item[1] == name and item[4] == password:
    return render_template('painel_user.html')
    #     else:
            # return render_template('index.html')
@app.route('/reservar/lab')
def reservar_labs(): 
    lista_labs = database.show_all_labs()
    view_lista_labs =[]
    print(lista_labs)
    return render_template('reservar_labs.html',mensagem=lista_labs)

@app.route('/cadastro')
def cadastro(): 
    return render_template('cadastro.html')

@app.route('/update_users')
def update_users(): 
    users = database.show_all()
    return render_template('update_users.html',mensagem=users)

@app.route('/delete_users')
def delete_users(): 
    users = database.show_all()
    return render_template('delete_user.html',mensagem=users)
@app.route('/unable_users')
def unable_users(): 
    users = database.show_all()
    return render_template('desativar_usuario.html',mensagem=users)
@app.route('/enable_users')
def enable_users(): 
    users = database.show_all_inactive()
    return render_template('ativar_usuario.html',mensagem=users)

@app.route('/unable_labs')
def unable_labs(): 
    users = database.show_all_labs()
    return render_template('desativar_lab.html',mensagem=users)
@app.route('/enable_labs')
def enable_labs(): 
    users = database.show_all_labs_inactive()
    return render_template('ativar_lab.html',mensagem=users)

@app.route('/cadastro/lab')
def cadastro_lab(): 
    return render_template('cadastro_lab.html')

@app.route('/update_labs')
def update_labs(): 
    labs = database.show_all_labs()
    return render_template('update_labs.html',mensagem=labs)

@app.route('/delete_labs')
def delete_labs(): 
    labs = database.show_all_labs()
    return render_template('delete_labs.html',mensagem=labs)

#CRUD USER
@app.route('/submit/cadastro', methods=['POST'])
def submit_cadastro():
    name = request.form['name'] +" " + request.form['lastName']
    email = request.form['email']
    cpf_cnpj = request.form['cpf']
    password = request.form['password'] 
    phone = request.form['celular']
    user_type_id= 0
    is_active= 1
    database.add_user(name,email,user_type_id,password,is_active,cpf_cnpj,phone)    
    return render_template('teste.html',mensagem=name)

@app.route('/submit/read_users', methods=['GET'])
def submit_read_users():
    lista_users = database.show_all()

    return render_template('consultar_usuarios.html',mensagem=lista_users)

@app.route('/submit/update_users', methods=['POST'])
def submit_update_users():
    field = request.form['field']
    name = request.form['name']
    id = request.form['id']
    print(id)
    lista = database.show_all()
    print('lista:', lista[1][1])
    for item in lista:
        print('ITEM 0:',item[0],'\n')
        print(item[1])
        print(id)
        if id == item[1]:
            id=item[0]
    database.update_user(field,name,id)
    return render_template('teste.html',mensagem=name)

@app.route('/submit/delete_users', methods=['POST'])
def submit_delete_users():
    id = request.form['id']
    print(id)
    lista = database.show_all()
    for item in lista:
        print('ITEM 0:',item[0],'\n')
        print(item[1])
        print(id)
        if id == item[1]:
            id=item[0]
    database.delete_user(id)
    return render_template('teste.html',mensagem=id)

@app.route('/submit/unable_labs', methods=['POST'])
def submit_unable_labs(): 
    users = database.show_all_labs()
    field = "is_active"
    name = "0"
    id = request.form['id']
    for item in users:
        if id == item[2]:
            id=item[0]
    database.update_lab(field,name,id)
    print(users)
    return render_template('teste.html',mensagem=users)


@app.route('/submit/enable_labs', methods=['POST'])
def submit_enable_labs(): 
    users = database.show_all_labs_inactive()
    field = "is_active"
    name = "1"
    id = request.form['id']
    for item in users:
        if id == item[2]:
            id=item[0]
    database.update_lab(field,name,id)
    print(users)
    return render_template('teste.html',mensagem=users)

@app.route('/submit/unable_users', methods=['POST'])
def submit_unable_users(): 
    users = database.show_all()
    field = "is_active"
    name = "0"
    id = request.form['id']
    for item in users:
        if id == item[1]:
            id=item[0]
    database.update_user(field,name,id)
    print(users)
    return render_template('teste.html',mensagem=users)

@app.route('/submit/enable_users', methods=['POST'])
def submit_enable_users(): 
    users = database.show_all_inactive()
    field = "is_active"
    name = "1"
    id = request.form['id']
    for item in users:
        if id == item[1]:
            id=item[0]
    database.update_user(field,name,id)
    #print(users)
    return render_template('teste.html',mensagem=users)

#CRUD lab
@app.route('/submit/cadastro/lab', methods=['POST'])
def submit_cadastro_lab():
    andar = request.form['andar']
    lab= request.form['lab']
    description= request.form['description']
    is_active='1'
    database.add_lab(andar,lab,description,is_active)    
    return render_template('teste.html',mensagem=lab)

@app.route('/submit/read_labs')
def submit_read_labs():
    lista_labs = database.show_all_labs()
    view_lista_labs =[]
    print(lista_labs)
    return render_template('consultar_labs.html',mensagem=lista_labs)

@app.route('/submit/update_lab', methods=['POST'])
def submit_update_lab():
    field = request.form['field']
    name = request.form['name']
    id = request.form['id']
    lista = database.show_all_labs()
    for item in lista:
        if id == item[2]:            
            id=item[0]
    database.update_lab(field,name,id)
    return render_template('teste.html',mensagem=name)

@app.route('/submit/delete_labs', methods=['POST'])
def submit_delete_labs():
    id = request.form['id']
    print(id)
    lista = database.show_all()    
    database.delete_lab(id)
    return render_template('teste.html',mensagem=id)
#Reserva LAB
@app.route('/read_labs_byuser')
def submit_read_labs_byuser():
    lista_labs = database.show_all_labs()
    view_lista_labs =[]
    print(lista_labs)
    return render_template('read_labs_byuser.html',mensagem=lista_labs)

@app.route('/submit/reserva', methods=['POST'])
def reserva():
    # id_data = request.form['date']
    id_lab = request.form['id']
    # arq = open("user.txt", "r")
    # user = arq.read()
    # print(id_data, id_lab, arq)
    # user.close()

    url = "https://api-go-wash-efc9c9582687.herokuapp.com/api/pay-boleto"

    payload = json.dumps({
    "user_id": 12,
    "lab_id": 1,
    "boleto": "12345678"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Vf9WSyYqnwxXODjiExToZCT9ByWb3FVsjr',
    'Cookie': 'gowash_session=Geh73kUQdqOapKPUDW1gIj7X4X3WNmbYCWStcuwl'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    res = json.loads(response.text)

    if res["data"]["status"] == "approved":
        database.createReserva(res["data"]["user_id"],id_lab,res["data"]["payment_date"])
    else:
        return print("erro")
    
    return render_template('read_labs_byuser.html')






if __name__ == '__main__':
    app.run(debug=True)
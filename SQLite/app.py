import database
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='../template')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/painel_admin')
def painel_admin():
    return render_template('painel.html')

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

@app.route('/cadastro/lab')
def cadastro_lab(): 
    return render_template('cadastro_lab.html')

@app.route('/unable_users')
def unable_users(): 
    users = database.show_all()
    return render_template('desativar_usuario.html',mensagem=users)


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
def submit_read_labss():
    lista_labs = database.show_all_labs()
    view_lista_labs =[]
    for itens in lista_labs:
        view_lista_labs.append(itens[2])
    return render_template('consultar_usuarios.html',mensagem=view_lista_labs)

@app.route('/submit/update_lab', methods=['POST'])
def submit_update_lab():
    field = request.form['field']
    name = request.form['name']
    id = request.form['id']
    print(id)
    lista = database.show_all_labs()
    print('lista:', lista[1][1])
    for item in lista:
        print('ITEM 0:',item[0],'\n')
        print(item[1])
        print(id)
        if id == item[1]:
            id=item[0]
    database.update_user(field,name,id)
    return render_template('teste.html',mensagem=name)

if __name__ == '__main__':
    app.run(debug=True)
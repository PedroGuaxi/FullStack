import database
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='../template')


@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/submit/read_users', methods=['POST'])
def submit_read_users():
    name = request.form['name']
    password = request.form['password']     
    return render_template('teste.html',mensagem=password)

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
    print(id)
    database.update_user(field,name,id)
    return render_template('teste.html',mensagem=name)

@app.route('/submit/delete_users', methods=['POST'])
def submit_delete_users():
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
    print(str(id))
    database.delete_user(id)
    return render_template('teste.html',mensagem=id)




if __name__ == '__main__':
    app.run(debug=True)
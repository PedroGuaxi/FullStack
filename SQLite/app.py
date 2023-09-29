import database
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='../template')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['name']
    password = request.form['password']    
    teste = database.show_all()  

    print(len(teste))
    for itens in teste:
        print(itens)
    return render_template('teste.html', mensagem=teste)  
if __name__ == '__main__':
    app.run(debug=True)
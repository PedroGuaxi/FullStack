import sqlite3

def show_all():
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  #query the database
  cursor.execute("SELECT * FROM users")
  items = cursor.fetchall()
  #commit command show all users
  conection.commit()
  #close our connection
  conection.close()
  return items
def add_user(name,email,user_type_id,password,is_active,cpf_cnpj,phone):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  #inter a user in user table
  cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)",(name,email,user_type_id,password,is_active,cpf_cnpj,phone))
  #commit command create user
  conection.commit()
  #close our connection
  conection.close()
def delete_user(id):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  cursor.execute("DELETE FROM users WHERE rowid = (?)", id)
  #commit command delete user
  conection.commit()
  #close our connection
  conection.close()
def update_user(field,name,id):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  teste ="UPDATE users SET "+field+"= (?) WHERE rowid = (?)"
  cursor.execute(teste, (name,id))
  #commit command delete user
  conection.commit()
  #close our connection
  conection.close()

#create a table
# 5 datatypes in SQLite : null(não existe), integer(number),real(decimal), text(texto),blob(mp3,image e etc.)
# cursor.execute("""CREATE TABLE users (
#                name DATATYPE text ,
#                email DATATYPE text ,
#                user_type_id DATATYPE integer,
#                password DATATYPE text ,
#                is_active DATATYPE integer ,
#                cpf_cnpj DATATYPE text ,
#                phone text DATATYPE integer
# )
# """)
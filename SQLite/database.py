import sqlite3

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

def show_all():
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  #query the database
  cursor.execute("SELECT rowid, * FROM users WHERE is_active= 1 ")
  items = cursor.fetchall()
  print(items)
  #commit command show all users
  conection.commit()
  #close our connection
  conection.close()
  return items

def update_user(field,name,id):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  query ="UPDATE users SET "+field+"= (?) WHERE rowid = (?)"
  cursor.execute(query, (name,id))
  #commit command delete user
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



#CRUD pra tabela lab
def add_lab(andar,lab,description,is_active):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  #inter a user in user table
  cursor.execute("INSERT INTO lab VALUES (?,?,?,?)",(andar,lab,description,is_active))
  #commit command create user
  conection.commit()
  #close our connection
  conection.close()

def show_all_labs():
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  #query the database
  cursor.execute("SELECT rowid, * FROM lab")
  items = cursor.fetchall()
  #commit command show all users
  conection.commit()
  #close our connection
  conection.close()
  return items
def update_lab(field,name,id):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  query ="UPDATE lab SET "+field+"= (?) WHERE rowid = (?)"
  cursor.execute(query, (name,id))
  #commit command delete user
  conection.commit()
  #close our connection
  conection.close()
def delete_lab(id):
  #conection = sqlite3.connect(':memory:')
  conection = sqlite3.connect('LabProject')
  #create a cursor
  cursor = conection.cursor()
  cursor.execute("DELETE FROM lab WHERE rowid = (?)", id)
  #commit command delete user
  conection.commit()
  #close our connection
  conection.close()


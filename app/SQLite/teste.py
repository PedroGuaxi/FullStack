# import database, sqlite3
# #create a table
# # 5 datatypes in SQLite : null(não existe), integer(number),real(decimal), text(texto),blob(mp3,image e etc.)
# conection = sqlite3.connect('LabProject')
#create a cursor
# cursor = conection.cursor()
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
# cursor.execute("""CREATE TABLE lab (
#                andar DATATYPE integer ,
#                lab DATATYPE text ,
#                description DATATYPE text,
#                is_active DATATYPE integer 
# )
# """)

# cursor.execute("""CREATE TABLE reserva (
#                user_id DATATYPE integer ,
#                lab_id DATATYPE integer ,
#                date DATATYPE text              
# )
# """)
# print(database.show_all_labs())
# conection.commit()
#close our connection
# conection.close()
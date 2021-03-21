import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')


cursor = connection.cursor()
# sql_query = 'INSERT INTO persona (nombre, primer_apellido, email) VALUES (\'Hero\', \'Rising\', \'f.stone@hiworld.com\');'
sql_query = 'INSERT INTO persona (nombre, primer_apellido, email) VALUES (%s, %s, %s);'
name = input('Enter your name: ')
last_name = input('Enter your last name: ')
email = input('Enter your email: ')
tuple_values = (name, last_name, email)
cursor.execute(sql_query, tuple_values)
connection.commit()

registros = cursor.rowcount
print(f'Registros insertados: {registros}')

cursor.close()
connection.close()
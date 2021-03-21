import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='admin',
                              host='127.0.0.1',
                              port='5432',
                              database='test_db')


'''un curso basicamente es un objeto que basicamente
    nos permitira ejecutar sentencia sobre la base
    de datos 
'''

# Open a cursor to perform database operations, DELETE, INSERT, UPDATE AND ETC
cursor = connection.cursor()  # object cursor
sql_query = 'SELECT * FROM persona'
cursor.execute(sql_query)  # execute the query

data = cursor.fetchall()  # get data
# conn.commit()

for record in data:
    print(record)
    
print(data)

cursor.close()
connection.close
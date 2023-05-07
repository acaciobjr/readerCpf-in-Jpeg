import mysql.connector

# Conectar ao banco de dados
connection = mysql.connector.connect(
    user='script_documentos',
    password='123',
    host='127.0.0.1',
    database='documentos_escaneados'
)

if connection.is_connected():
    print('Conexão bem sucedida ao banco de dados')
else:
    print('Erro de conexão ao banco de dados')
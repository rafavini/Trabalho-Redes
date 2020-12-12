from socket import *
HOST = 'localhost'
PORT = 50000
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) #escuta apenas uma conexão
print('esperando alguma conexão')
conn, ender = s.accept() #aceita a conexão com o cliente
print('foi estabelecida conexão com',ender)
while 1:
    sentence = conn.recv(1024) #recebe texto do cliente
    sentence = sentence.decode('utf-8')
    if sentence == 'criar':
        print('Cliente usou comando de criar um diretorio')
        conn.send('comando aceito'.encode('utf-8'))
    elif sentence == 'remove':
        print('Cliente usou comando de remover um directorio')
        conn.send('comando aceito'.encode('utf-8'))
    elif sentence == 'ls':
        print('Cliente usou o comando de listagem')
        conn.send('comando aceito'.encode('utf-8'))
    elif sentence == 'quit':
        print('Conexão encerrada')
        conn.close()
        break
    else:
        print('Cliente utilizou um comando invalido')
        conn.send('comando invalido'.encode('utf-8'))

s.close()

from socket import *
import os
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta
s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    sentence = input('Digite um comando: ')
    sentence2 = sentence.split() # separa o texto
    s.send(sentence2[0].encode('utf-8')) #envia texto para o servidor

    mensagem = s.recv(1024) #recebe resposta do servidor

    mensagem = mensagem.decode('utf-8') #decodifica mensagem do servidor
   
    if sentence2[0] == 'criar':
        path = os.getcwd() #pega o caminho do arquivo que esta executando
        directoryName = path+'/'+sentence2[1] #concatena com o nome que foi passado
        os.mkdir(directoryName) #cria o diretorio
    elif sentence2[0] == 'remove':
        path = os.getcwd()
        directoryName = path+'/'+sentence2[1]
        os.rmdir(directoryName) #remove o diretorio
    elif sentence2[0] == 'ls':
        path = os.getcwd()
        arquivos = os.listdir(path)
        for i in range(len(arquivos)):
            print(arquivos[i])  #lista os arquivos dentro do diretorio
    elif sentence2[0] == 'quit': #finaliza o cliente
        break

    if mensagem == 'comando invalido': #caso tenha algum comando não programado dar comando invalido
        print("comando invalido")
    
    
s.close()
    

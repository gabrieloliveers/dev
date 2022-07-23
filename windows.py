import subprocess
import csv
import pwd
import random

#1 - Abre o arquivo CSV
file = open('users.csv')

#2- Lê o arquivo CSV e Traz pra variavel lines uma lista com todas a listas
lines = csv.reader(file)

#3- Traz todos os usuários do sistema, e cria um lista com apenas a posição 0 que são os nomes (usernames)
usernames = [username[0] for username in pwd.getpwall()]

#4- Aqui seta todas os caracteres que a senha aleatória deve conter
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"

#5- Aqui seta a quantidade de caracteres que a senha deve ter
password_length = 12

print('USUÁRIOS CRIADOS:')
print("")

#6- Percorre a lista de lines para trazer o nome e o email dos usuários
for line in lines:
    name = line[0]
    email = line[2]

    #5- Extrai o username atravéz do email, removendo o "@gmail.com" do final
    username = email.replace("@gmail.com", "")

    #6- Condição para verificar se o usuário existe ou não para fazer a criação do mesmo no linux
    if username in usernames:
        print('Usuário já existe:', username)
        print("")    
    else:
        #7- Gera um senha aleatória e agrupa a lista da senha em uma string só ("".join agrupa a lista que o random devolve em uma string)        
        password = "".join(random.sample(characters, password_length))

        #8- Roda um comando no linux para a criação de usuário já setando uma senha aleatória gerada anteriormente
        subprocess.run(['sudo', 'useradd', username, '-p', password])
        print("Usuário:", username)
        print("Senha:", password)
        print("")
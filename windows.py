import wmi
import os
import csv
import random

#1 - Abre o arquivo CSV
file = open('users.csv')

#2- Lê o arquivo CSV e Traz pra variavel lines uma lista com todas a listas
lines = csv.reader(file)

#3- Utilização do WMI para Trazer todos os usuários do sistema e em seguida eu crio uma lista vazia e adiciono o nome dos usuários com o append (usernames)
usernames = []
windows=wmi.WMI()
for user in windows.Win32_UserAccount(["Name"]):
    usernames.append(user.Name)

#4- Aqui seta todas os caracteres que a senha aleatória deve conter
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#5- Aqui seta a quantidade de caracteres que a senha deve ter
password_length = 12

print('USUÁRIOS CRIADOS:')
print("")

#6- Percorre a lista de lines para trazer o nome e o email dos usuários
for line in lines:
    name = line[0]
    email = line[2]

    #7- Extrai o username atravéz do email, removendo o "@gmail.com" do final
    username = email.replace("@gmail.com", "")

    #8- Condição para verificar se o usuário existe ou não para fazer a criação do mesmo no linux
    if username in usernames:
        print('Usuário já existe:', username)
        print("")    
    else:
        #9- Gera um senha aleatória e agrupa a lista da senha em uma string só ("".join agrupa a lista que o random devolve em uma string)        
        password = "".join(random.sample(characters, password_length))

        #10- Roda um comando no windows para a criação de usuário já setando uma senha aleatória gerada anteriormente
        os.system(f'net user {username} {password} /add')
        print("Usuário:", username)
        print("Senha:", password)
        print("")
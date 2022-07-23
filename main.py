import subprocess
import csv
import pwd

#1
file = open('users.csv')
#2
lines = csv.reader(file)
#3
usernames = [username[2] for username in pwd.getpwall()]
#4
for line in lines:

    name = line[0]
    email = line[2]
    #5
    username = email.replace("@gmail.com", "")
    #6
    if username in usernames:
     print('Usuário já existe')    
    else:
     subprocess.run(['sudo', 'useradd', username])
     print('Usuários criados com sucesso')
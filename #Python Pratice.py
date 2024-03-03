#Password Checker

MyPassword = {'zak-sm': 'mint123', 'fi-oby': 'rose123', 'al-kel': 'blue123'}

def PasswordCheck():
    user = str(input('Enter Username: '))
    if user in MyPassword:
        password = input('Enter Password: ')
        if MyPassword[user] == password:
            print('Access Granted!')
        else:
            print('Incorrect Password')
    else: print('No User Found')
    
PasswordCheck()

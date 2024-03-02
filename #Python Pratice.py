#Password Checker

MyPassword = {'password': 'zkal0307'}

def PasswordCheck(attempt:str):
    
    if attempt in MyPassword['password']:
        print('Access Granted')
    else:
        print('Incorrect Password')
    
PasswordCheck(attempt = input('Input Passsword: '))
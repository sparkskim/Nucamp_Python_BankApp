'''
Workshop 2 - Banking Applet
By Sung Kim
Date 8/13/2022
'''


def show_balance(balance):
    '''
    display the account balance of the logged-in user
    '''
    balance = float()
    print(balance)


def deposit(balance):
    '''
    prompt user input deposit value
    '''
    amount = input('Enter amount to deposit: $')
    return balance + float(amount)


def withdraw(balance):
    '''
    promt user input withdraw value
    '''
    amount = input('Enter amount to withdraw: $')
    if int(amount) > balance:
        print('Where are you going to get that kind of money?')
    else:
        return balance - float(amount)


def logout(name):
    '''
    logout
    '''
    print(f'Goodbye! {name}')

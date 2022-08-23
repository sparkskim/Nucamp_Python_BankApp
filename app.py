'''
Workshop 2 - Banking Applet
By Sung Kim
Date 8/13/2022
'''

from banking_pkg.account import show_balance, deposit, withdraw, logout

print("          === Automated Teller Machine ===          ")

BALANCE = 0.0

# Prompt user to register
while True:
    NAME = input('Enter your name to register: ')
    if len(NAME) > 10:
        print('The maximum name length is 10 characters.')
    else:
        break
while True:
    PIN = input('Enter PIN: ')
    if len(PIN) > 4:
        print('PIN must contain 4 numbers.')
    else:
        break
print(f'{NAME} has been registered with a starting balance of {BALANCE}')

# Prompt user to log in and display menu options upon valid login
print('LOGIN')
while True:
    user_inputName = input('Enter name: ')
    user_inputPin = input('Enter PIN: ')
    if user_inputName == NAME and user_inputPin == PIN:
        print('Login successful!')
        break
    print('Invalid credentials!')


def atm_menu(user):
    '''
    Function that visually displays options to user
    '''
    print('')
    print('          === Automated Teller Machine ===          ')
    print(f'User: {NAME}')
    print('------------------------------------------')
    print('| 1.    Balance     | 2.    Deposit      |')
    print('------------------------------------------')
    print('------------------------------------------')
    print('| 3.    Withdraw    | 4.    Logout       |')
    print('------------------------------------------')


# Prompt the user to choose an option
while True:
    atm_menu(user)
    option = input('Choose an option: ')

    if option == '1' or option == 'Balance'.lower():
        show_balance(BALANCE)
    elif option == '2' or option == 'Deposit'.lower():
        BALANCE = deposit(BALANCE)
        print(f'Current balance: {BALANCE}')
    elif option == '3' or option == 'Withdraw'.lower():
        BALANCE = withdraw(BALANCE)
        print(f'Current balance: {BALANCE}')
    elif option == '4' or option == 'Logout'.lower():
        logout(NAME)
        break

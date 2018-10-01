from sys import *

while True :
    print('終了するにはexitと入力してください。')
    response = input()
    if response == 'exit':
        exit()
    print(response + 'と入力されました。')

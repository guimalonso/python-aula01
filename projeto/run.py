from banco import *
import threading

if __name__ == "__main__":
    user = input('Nickname: ')
    f = threading.Thread(target=busca_mensagens)
    f.start()

    while f.isAlive:
        mens = input()
        cadastrar(user, mens)
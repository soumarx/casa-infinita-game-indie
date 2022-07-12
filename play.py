import time
import eventos

eventos.introducao()


def entrada_casa():
    ans = 'incorrect'
    while ans == 'incorrect':
        print("\n(1) Entrar na Casa (2) Desistir de entrar na Casa")
        c1 = input()
        if c1.upper() == "1":
            ans = 'correct'
            eventos.quarto1()
        elif c1.upper() == "2":
            ans = 'correct'
            eventos.volta_casa()
        else:
            print("Escolha uma ação!")


def decisao_casa():
    ans = 'incorrect'
    while ans == 'incorrect':
        print("\n(1) Voltar para a Casa Estranha (2) Ir para cama")
        c1 = input()
        if c1.upper() == "1":
            time.sleep(3)
            print("\nDecidir voltar para o meu carro e retornar para aquela casa")
            ans = 'correct'
            eventos.quarto1()
        elif c1.upper() == "2":
            time.sleep(3)
            print("\nDecidir ir tomar banho e dormir")
            time.sleep(3)
            print("\nSó um tolo pra cair em uma brincadeira dessas")
            ans = 'correct'
            eventos.dormir()
        else:
            print("Escolha uma ação!")


def scene2():
    print("")
    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    pick = ''
    while ans == 'incorrect':
        if c1.upper() == "PICK":
            print("")
            time.sleep(2)
            print("")
            ans = 'correct'
            pick = "True"
        elif c1.upper() == 'IGNORE':
            print("")
            ans = 'correct'
            pick = "False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1 = input()
    time.sleep(2)
    scene3(pick)


def scene3(pick_value):
    print("")
    time.sleep(2)
    if pick_value == "True":
        time.sleep(2)
        print("")
        time.sleep(2)
        print("")
    elif pick_value == "False":
        print("")


def continuar():
    ans = 'incorrect'
    while ans == 'incorrect':
        print("\n(1) Reiniciar Jogo (2) Desistir")
        c1 = input()
        if c1.upper() == "1":
            ans = 'correct'
            eventos.introducao()
        elif c1.upper() == "2":
            ans = 'correct'
        else:
            print("Escolha uma ação!")


eventos.introducao()
print("\n\n")
print("===================FIM DO JOGO===================")

import eventos
import time


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


def olhar_atras():
    time.sleep(3)
    print("\n(1) Olhar para a porta de trás (2) Seguir em frente")
    c1 = input()
    ans = 'incorrect'
    olhou = ''
    while ans == 'incorrect':
        if c1.upper() == "1":
            time.sleep(3)
            print("\nPor incrível que pareça, a porta do qual eu vim, sumiu")
            time.sleep(3)
            print("\nPensei que poderia ter descido alguma cortina cobrindo a porta ou algo do tipo")
            time.sleep(3)
            print("\nMe mantive calmo, já que até agora, está tudo tão tranquilo")
            time.sleep(3)
            print("\nDecidir seguir mesmo com essa pulga atrás da orelha")
            ans = 'correct'
            olhou = "True"
        elif c1.upper() == '2':
            print("\nNem me incomodei em analisar tanto o quarto")
            time.sleep(3)
            print("\nEstá indo tudo bem, tudo parecendo apenas uma grande brincadeira de criança")
            time.sleep(4)
            ans = 'correct'
            olhou = "False"
        else:
            print("Escolha uma ação! Olhar ou seguir em frete")
            c1 = input()
    time.sleep(2)
    eventos.quarto3(olhou)


def escolher_porta():
    ans = 'incorrect'
    while ans == 'incorrect':
        print("\n(1) Escolher Porta de Madeira (2) Escolher Porta de Metal")
        c1 = input()
        if c1.upper() == "1":
            time.sleep(3)
            print("\nFui em direção a porta de madeira...")
            ans = 'correct'
            eventos.porta_madeira()
        elif c1.upper() == "2":
            time.sleep(3)
            print("\nFui em direção a porta de metal...")
            ans = 'correct'
            eventos.porta_metal()
        else:
            print("Escolha uma ação!")


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

import decisoes
import time


def introducao():
    print("Baseado na Creepypasta Casa sem Fim")
    time.sleep(2)
    print("2014")
    time.sleep(2)
    print("\nMeu amigo que não via online a semanas, me manda uma mensagem")
    time.sleep(4)
    print("\nBruno, cara, nós precisamos conversar!")
    time.sleep(4)
    print("\nFoi quando ele me disse sobre a Casa sem Fim")
    time.sleep(4)
    print("\nEla tinha esse nome pois ninguém nunca alcançou a saída final")
    time.sleep(4)
    print("\nAs regras eram simples: chegue na saída final e você ganha 5000 reais, nove cômodos no total")
    time.sleep(5)
    print("\nEu não acreditei nele. Por que eu deveria?")
    time.sleep(4)
    print("\nEu disse a ele que iria checar isso na outra noite")
    time.sleep(4)
    print("\n5000 reais soava bom demais pra ser verdade")
    time.sleep(4)
    print("\nNa noite seguinte...")
    time.sleep(3)
    print("\nQuando eu cheguei, imediatamente notei algo estranho sobre a casa")
    time.sleep(5)
    print("\nVocê já viu ou leu algo que não deveria te assustar, mas por alguma razão te gelava a espinha?")
    time.sleep(6)
    print("\nEntão pensei novamente...")
    time.sleep(3)

    decisoes.entrada_casa()


def quarto1():
    time.sleep(3)
    print("\nEu andei através da casa e o sentimento de mal estar apenas aumentou quando eu abri a porta da frente")
    time.sleep(5)
    print("\nMeu coração desacelerou e soltei um suspiro aliviado assim que entrei")
    time.sleep(4)
    print("\nO cômodo parecia como uma entrada de um hotel normal decorada para o Halloween")
    time.sleep(5)
    print("\nUm sinal foi colocado no lugar onde deveria ter um funcionário")
    time.sleep(4)
    print("\nSe lia: você já está no primeiro comodo. Mais oito a seguir")
    time.sleep(4)
    print("\nAlcance o final e você vence!")
    time.sleep(4)
    print("\nEu ri e fui para a primeira porta")
    time.sleep(4)

    quarto2()


def quarto2():
    time.sleep(3)
    print("\nA segunda área era quase cômica")
    time.sleep(3)
    print("\nA decoração lembrava o corredor de Halloween")
    time.sleep(3)
    print("\nCheia de fantasmas de lençol e zumbis robóticos")
    time.sleep(3)
    print("\nNo outro lado tinha uma saída, a única porta além da qual eu entrei")
    time.sleep(3)
    print("\nBateu a curiosidade de olhar para trás...")

    decisoes.olhar_atras()


def quarto3(olhou):
    time.sleep(3)
    print("\nPassei através das falsas teias de aranha e fui para o terceiro quarto")
    time.sleep(3)
    print("\nFui recebido por uma névoa assim que abri a porta do terceiro quarto")
    time.sleep(3)
    print("\nNão havia apenas uma máquina de fumaça...")
    time.sleep(3)
    print("\nMas também morcegos pendurados pelo teto e girando em círculos. Assustador!")
    if olhou == "True":
        time.sleep(3)
        print("\nLembrei que a porta tinha sumido no quarto anterior")
        time.sleep(3)
        print("\nMesmo que eu queira voltar agora, voltaria para o quarto 2 mas não conseguiria ir mais adiante")
        time.sleep(3)
        print("\nAo menos é o que o pessoal que cuida dessa casa queira que eu pense...")
    time.sleep(3)
    print("\nHavia uma trilha uma trilha sonora em loop de Halloween que qualquer um encontra em uma loja de R$1,99")
    time.sleep(4)
    print("\nEu vi que esse quarto era diferente pois tinha duas portas a frente")
    time.sleep(3)
    print("\nUma com a porta de madeira, com aspecto bem antigo")
    time.sleep(3)
    print("\nE uma porta de metal, não parecia aquelas porta de alumino mas sim metal puro")
    time.sleep(3)

    decisoes.escolher_porta()


def porta_madeira():
    time.sleep(3)


def porta_metal():
    time.sleep(3)


def volta_casa():
    time.sleep(3)
    print("\nDecidi voltar para o meu carro e retornar para minha casa")
    time.sleep(4)
    print("\nQuem daria tanto dinheiro para qualquer um chegar ao final de uma casa?!")
    time.sleep(4)
    print("\nSó poderia ter alguma pegadinha")
    time.sleep(4)
    print("\nChegando em casa...")
    time.sleep(3)
    print("\nPensei muito no caminho, quantidade de dinheiro seria de grande ajuda")
    time.sleep(4)
    print("\nNão que eu iria ficar rico com essa quantia")
    time.sleep(4)
    print("\nMas fora isso, se fosse alguma pegadinha")
    time.sleep(4)
    print("\nAo menos poderia parar de pensar que eu realmente poderia ganhar essa quantia em apenas alguns minutos")
    time.sleep(4)

    decisoes.decisao_casa()


def dormir():
    time.sleep(3)
    print("\nNo dia seguinte...")
    time.sleep(4)
    print("\nDecidir chamar o meu amigo e apenas vi que nem ao menos ele recebeu minhas mensagens")
    time.sleep(4)
    print("\nIsso durou dias, então resolvi esquece-lo")
    time.sleep(4)
    print("\nSimplesmente ele voltou do nada falando sobre a casa e sumiu")
    time.sleep(4)
    print("\nComo de costume...")
    time.sleep(5)

    decisoes.continuar()

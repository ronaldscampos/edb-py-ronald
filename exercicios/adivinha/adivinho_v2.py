import random

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

card1 = [1, 3, 5, 7, 9, 11, 13, 15]
card2 = [2, 3, 6, 7, 10, 11, 14, 15]
card3 = [4, 5, 6, 7, 12, 13, 14, 15]
card4 = [8, 9, 10, 11, 12, 13, 14, 15]




#### links utilizados
# https://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-random-numbers-without-duplicates
# https://docs.python.org/3/howto/sorting.html
# https://towardsdatascience.com/switch-case-statements-are-coming-to-python-d0caf7b2bfd3

# funcao para geracao dos valores nos cards
def generate_cards(qtdCards, maxNum):
    lstCards = [] 

    #gerando cards aleatorios, dentro do range e da quantidade informada
    for i in range(0, qtdCards):
        tmpLst = random.sample(range(1, maxNum), 8)
        lstCards.append(sorted(tmpLst))
    return lstCards


# nova funcao de advinhar 
def advinhar_2(lstCards):
    resultado = 0
    fator = 1
    for card in lstCards:
        resposta = input(f'O número esta aqui? (S/N) -> {card} ')
        if resposta.upper() == 'S':
            resultado = resultado + fator
        fator = fator * 2
    print(f'Você pensou no número: {resultado}')



def print_ask(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Olá, {name}')  # Press Ctrl+8 to toggle the breakpoint.
    print(name)


def advinhar():
    resultado = 0

    r1 = input(f'O numero está aqui? (S/N) -> {card1}')
    if r1.upper() == "S":
        resultado = resultado + 1

    r2 = input(f'O numero está aqui? (S/N) -> {card2}')
    if r2.upper() == "S":
        resultado = resultado + 2

    r3 = input(f'O numero está aqui? (S/N) -> {card3}')
    if r3.upper() == "S":
        resultado = resultado + 4

    r4 = input(f'O numero está aqui? (S/N) -> {card4}')
    if r4.upper() == "S":
        resultado = resultado + 8

    print(f'Você pensou no número: {resultado}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    qtdCards = int(input('Olá, vamos jogar um jogo? Quantos cards deseja utiliza? '))
    print(f'Você escolheu {qtdCards} cards')

    #definindo numero maximo do range de aleatorios
    maxNum = 0
    if qtdCards == 7:
        maxNum = 127
    elif qtdCards == 6:
        maxNum = 63
    elif qtdCards == 5:
        maxNum = 31
    else:
        maxNum = 15

    lstCards = generate_cards(qtdCards, maxNum)

    print(f'Pense em um número entre 1 e {maxNum}...')

    ja_pensou = input('E ai, já pensou? (S/N) ')

    if ja_pensou.upper() != "S":
        print('Pois ande logo!')
    else:
        print('Não vai esquecer o número...')

    #advinhar()
    advinhar_2(lstCards)

    correto = input(f'Acertei? (S/N)')
    if correto.upper() == "S":
        print('Eu sou demais!!! ;-)')

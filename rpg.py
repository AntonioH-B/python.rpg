import os
import sys
import time
from rpgrepo import *

class cor:
    blackbg = "\033[0;40m"
    redbg = "\033[0;41m"
    greenbg = "\033[0;42m"
    bluebg = "\033[0;44m"

    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    brown = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    closed = '\033[m'
    n = ''

def batalha():
    prob_attack_player = perc([100, 50, 49, 1, 0])
    prob_attack_enemy = perc([100, 50, 49, 1, 0])
    prob_enemy = perc([100, 1, 90, 1,0])
    return prob_attack_player, prob_attack_enemy, prob_enemy

def color(a, b):
    return b + str(a) + cor.closed

def animated_text(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

live = 10
mlive = 50

velocidade = 0
vida = 0
forca = 0
resistencia = 0
inteligencia = 0
dano = 0
chave = False

class enemy_base:
    mlife = 100
    forca = 10
    resistencia = 10

class ladrao: 
    mlife
    forca = 9
    resistencia = 10
    inteligencia = 12
class piromante: 
    mlife = 100
    forca = 12
    resistencia = 12
    inteligencia = 1
class feiticeiro: 
    mlife = 80
    forca = 9
    resistencia = 8
    inteligencia = 15
class guerreiro: 
    mlife = 110
    forca = 13
    resistencia = 11
    inteligencia = 9
class machado:
    dano = 20
    velocidade = 10
class espada:
    dano = 15
    velocidade = 15
class adaga:
    dano = 13
    velocidade = 20
class lanca:
    dano = 15
    velocidade = 13



vida, classe = 0, ''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

nome_usuario = input('Digite seu nome: ')
clear()

print('========Seja Bem-vindo', nome_usuario,'==========')



cont = 1 
for cont in range(0,1):
    def upd():
        global mlife, life, lifebar
        lifebar = {1 : numbar(life, 0, mlife, [green,blue,red]), 2 : bar(life, 0, mlife, [greenbg,bluebg,red])}
        return lifebar
    
    upd()

    print(lifebar[1], '\n', lifebar[2])

    print(color('.feiticeiro          ', cor.purple),color('.guerreiro', cor.blue))
    print(color('.ladrao      ', cor.cyan),color('.piromante', cor.green))
    classe = input('Qual classe você deseja jogar?: ') 

    if classe == 'ladrao':
        classe = ladrao
        cont = 0
    elif classe == 'piromante':
        classe = piromante
        cont = 0
    elif classe == 'guerreiro':
        cont = 0
        classe = guerreiro
    elif classe == 'feiticeiro':
        cont = 0
        classe = 'feiticeiro'
    else: 
        cont = 1

    print(f'{color(live * '_', cor.greenbg)}')
clear()
    
for cont in range(0,1):

    upd()

    print(lifebar[1], '\n', lifebar[2])

    print(color('.Adaga',cor.blue),color('.Espada',cor.brown))
    print(color('.Machado',cor.cyan),color('.Lanca',cor.green))
    arma = input('Qual arma você deseja jogar?: ')
    if arma == 'machado':
        arma = machado
        cont = 0
    elif arma == 'espada':
        arma = espada
        cont = 0
    elif arma == 'adaga':
        cont = 0
        arma = adaga
    elif arma == 'lanca':
        arma = lanca
        cont = 0
    else: 
        cont = 1

        print(f'{color(live * '_', cor.greenbg)}')

clear()

text1 = 'Você acorda em uma cela, junto a você só a um esqueleto de outro prisioneiro.\nVocê olha para grade da cela e enxerga um homem querendo te da uma chave...\n\n\n\n\n'
animated_text(text1)

text2 = 'Estranho: pegue aqui nobre guerreiro, pegue essa chave e nos salve'
animated_text(text2)

clear()
while True:
    
    acao1 = int(input('pegar chave \n[1]sim \n[2]não\nResposta:  '))
    if acao1 == 1:
        text3 = (color('====Você pegou a chave====', cor.green))
        chave = True
        animated_text(text3)
        break
    elif acao1 == 2:
        text4 = ('Você perdeu a oportunidade de sair da cela\n')
        animated_text(text4)
        print(color('===================VOCÊ PERDEU==================', cor.red))
        break
    else:
        print(color('Resposta incorreta....',cor.red))

while True:
    
    prob_attack_player = perc([100, 50, 49, 1, 0])
    prob_attack_enemy = perc([100, 50, 49, 1, 0])
    prob_enemy = perc([100, 1, 90, 1,0])
    if prob_enemy == 1:

        upd()

        text5 = print('\n======================Você saí da cela e avista INIMIGO======================')
        acao2 = int(input('[1]Enfrentar\n[2]Correr\nResposta:  '))
        if acao2 == 1:
            print('VOCÊ ENTROU NA BATALHA.....')
            break
        elif acao2 == 2:
            print('akkakakakakakak você não tem escolha...')
        else:
            print('Resposta errada...')
        
        print(lifebar[1], '\n', lifebar[2])
        print(f'{color(live * '_', cor.greenbg)}')

while True:

    upd()
    print(lifebar[1], '\n', lifebar[2])

    text6 = color('AZURA',cor.red)
    print(enemy_base.mlife)

    acao3 = color('[1]Atacar\n[2]Correr',cor.green)
        if acao3 == 1:
            prob_attack_player

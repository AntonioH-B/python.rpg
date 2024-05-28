import os
import random

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

def color(a, b):
    return b + str(a) + closed


def title(m, e, t, d, c = []):
    if c == None:
        g = m//2 - len(t)
        return '{} {} {}'.format(e * g, t, d * g)
    elif c != None:
        g = m//2 - len(t) // 2
        return '{} {} {}'.format(color(e, c[0]) * g, color(t, c[1]), color(d, c[2] )* g)

def numbar(a, b, d, c = []):
    return '{}{}{}{}'.format(color(a, c[0]), '   ' + color(str(b), c[1]),  ' ' * (d-2), color(d, c[2]))    

def bar(a, b, d, c = []):
    return '{}{}{}'.format(color(' ' * (a - b), c[0]), color(' ' * b, c[1]), color('_' * (d-a), c[2]) )

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') 
    

def perc(b = []):
    g = random.randint(0,100)
    print(g)
    for c in range(0, len(b), 2):
        if c == len(b) - 2 or b[+2] < g:
            return b[c+1]          
def expc(a, b, c):
    if a == 1:
        b  += (b * c) / 100
    if isinstance(b, float):
        b = int(b) + 1
    return b

mlife = 50
life = 10

def upd():
    global mlife, life, lifebar
    lifebar = {1 : numbar(life, 0, mlife, [green,blue,red]), 2 : bar(life, 0, mlife, [greenbg,bluebg,red])}
    return lifebar

upd()
print(lifebar[1], '\n', lifebar[2])

life = 20
upd()

print(lifebar[1], '\n', lifebar[2])

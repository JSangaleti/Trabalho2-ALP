#!./bin/python

from codigo.analisador import *

def main():
    exemplo = 'Programação funcional utiliza funções. Funções podem ser combinadas e funções podem ser reutilizadas.'
    print(separar_palavras(exemplo))

if __name__ == '__main__':
    main()

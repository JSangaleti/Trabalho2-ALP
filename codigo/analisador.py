import re

def separar_palavras(texto: str) -> tuple:
    return tuple(re.findall(r'[^\W\d_]+', texto.casefold()))


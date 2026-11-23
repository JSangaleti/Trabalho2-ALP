import re
from functools import reduce

def separar_palavras(texto: str) -> tuple:
    return tuple(re.findall(r'[^\W\d_]+', texto.casefold()))

def contar_frequencias(palavras: tuple) -> dict:
    # Fold com função anônima, sem modificar as contagens anteriores.
    return reduce(
        lambda contagens, palavra: {
            **contagens,
            palavra: contagens.get(palavra, 0) + 1,
        },
        palavras,
        {},
    )
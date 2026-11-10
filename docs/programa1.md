# Parte 1

`casefold()` normaliza maiúsculas e minúsculas.
`re.findall(...)` extrai as palavras, preservando letras acentuadas.
`tuple(...)` produz uma coleção imutável.
`separar_palavras()` é uma função pura: recebe o texto e devolve o resultado, sem imprimir ou alterar dados externos.

Função pura: `separar_palavras(texto)` depende do texto recebido, devolve o resultado e não altera dados externos.
Estrutura imutável: o resultado é uma tupla de strings; seus elementos não podem ser substituídos.
Separação dos efeitos: o `print` fica fora da função de processamento.

| Conceito                      | Aplicação concreta                                                              |
| ----------------------------- | ------------------------------------------------------------------------------- |
| `map`                         | Normalizar cada palavra do texto.                                               |
| `filter`                      | Selecionar as palavras que não são stopwords.                                   |
| `reduce`                      | Construir a contagem de ocorrências.                                            |
| `lambda`                      | Informar o critério de ordenação das palavras.                                  |
| Funções de ordem superior     | Receber funções de transformação ou filtragem como parâmetros.                  |
| Composição                    | Combinar separação, normalização, filtragem e contagem para realizar a análise. |
| Imutabilidade e funções puras | Receber uma grade do Jogo da Vida e devolver outra, preservando a original.     |
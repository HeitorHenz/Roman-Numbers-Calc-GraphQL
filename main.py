import strawberry
import functools
import operator
import re


def achar_numero_romano(texto):

    texto_maiusculo = texto.upper()
    resultado_regex = re.findall("(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})", texto_maiusculo)
    numero_romano = []

    for resultados in resultado_regex:
        resultado_tratado = functools.reduce(operator.add, (resultados))
        if resultado_tratado != '':
            numero_romano.append(resultado_tratado)

    if(len(numero_romano) != 0):
        return numero_romano
    else:
        raise Exception('A entrada não apresentou um número romano válido')

def converter_numero(numero_romano):
    maior_numero = 0
    maior_resultado = 0
    for num in numero_romano:
        mapa_numeros_romanos = (('M', 1000), ('CM', 900),
            ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90),
            ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4), ('I', 1))
        resultado, indice = 0, 0
        for numero, valor in mapa_numeros_romanos:
            count = 0
            while num[indice: indice+len(numero)] == numero:
                count += 1
                resultado += valor
                indice += len(numero)
        if resultado > maior_resultado:
            maior_resultado = resultado
            maior_numero = num

    return maior_resultado,maior_numero

@strawberry.type
class NumeroRomano:
    number: str
    value: int

# Setando uma Query pois é obrigatório para se obter o retorno da Mutation 

@strawberry.type
class Query:
    @strawberry.field
    def query_requerimento() -> str:
        return ""

@strawberry.type
class Mutation:
    @strawberry.mutation
    def search(self, text: str) -> NumeroRomano:
        tem_numero = achar_numero_romano(text)
        value, number = converter_numero(tem_numero)
        return NumeroRomano(value=value, number=number)

schema = strawberry.Schema(query=Query, mutation=Mutation)


# -*- coding:utf-8 -*-
__author__ = 'mirwox'


"""Escreva uma função chamada par_balanceados(expressao) que
    recebe uma string contendo uma expressão com parênteses
    e devolve True se estiverem balanceados
    Vamos supor que não há espaços entre os parênteses
    Ex.: ((()))
    Ex.: )))()()

    A regra é - se vier um sinal de fechar parênteses e a pilha está vazia, a expressão não está balanceada
    Se vier um sinal de fechar parênteses e o elemento do topo da pilha for um sinal
    de abrir parênteses, removemos o topo da pilha
    Se vier um sinal de abrir parênteses, empilhamos

    Se ao final a pilha estiver vazia, estava balanceada

    Existe uma outra versão mais detalhada aqui:
    http://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html
    """


def balanceados(expressao):
    pilha = []

    for parentese in expressao:
        if parentese == ')':
            if pilha == []:
                return False
            elif pilha[-1] == '(':
                pilha.pop()
        if parentese == '(':
            pilha.append(parentese)

    if pilha == []:
        return True

# O exercicio já está resolvido, o código abaixo é só para testar

entrada = input("Digite uma expressão com parênteses para teste\n")
if balanceados(entrada):
    print ("Os parênteses estão balanceados")
else :
    print ("Os parênteses não estão balanceados")




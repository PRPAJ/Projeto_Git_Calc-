def calcule(a, b, op):
    if op == '+' or 'soma':
        return soma(a,b)
    elif op == '-' or 'subtracao':
        return subtracao(a,b)
    elif op == '*' or 'multiplicacao':
        return multiplicacao(a,b)
    elif op == '/' or 'divisao':
        return divisao(a,b)
    else:
        print('Operação inválida')

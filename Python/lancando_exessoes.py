#def dividir(n1, n2):
#    try:
#        print(f'Resultado: {n1 / n2}')
#    except ZeroDivisionError as erro:
        # print(f'Erro na Função: {erro}')
#        raise

#try:
#    dividir(10, 2)
#except Exception as erro:
#    print(f'Erro Desenvolvedor: {erro}')


def dividir(n1, n2):
    if n2 == 0:
        raise ValueError('Não é possível dividir por zero.')

    print(f'resultado: {n1/n2}')

#try:
#    dividir(10, 0)
#except ValueError as erro:
#    print(erro)


class OpcaoInvalidaError(Exception):
    pass


def seleciona_opcao(opcao):
    if opcao == '1':
        print('Cartoes de crédito')
    elif opcao == '2':
        print('Financiamentos')
    else:
        raise OpcaoInvalidaError('Opçao Invalida')


try:
    seleciona_opcao('3')
except OpcaoInvalidaError as erro:
    print(erro)


print('running')
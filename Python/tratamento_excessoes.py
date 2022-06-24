lista = ['Jamilton', 'Ana']
dicionario = {'nome': 'Franck'}


try:
    print(lista[2])
    # print(dicionario['teste'])
except (IndexError, KeyError) as erro:
    print('Item selecionado fora da lista')
except Exception as erro:
    print(f'Exception: {erro}')
else:
    print('Executou com sucesso!')
finally:
    print('Sempre vai executar!')

print('Running')

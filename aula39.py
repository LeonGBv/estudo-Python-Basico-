"""
    Iterando Strings com while
"""
#       01234567   
nome = 'Leonardo' # Iteráveis
#       87654321

tamanho_nome = len(nome)
#print(tamanho_nome)

#nova_string = '*L*'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
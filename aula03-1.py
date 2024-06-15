# #Listas
vendas = [100, 50, 14, 20,  30, 700]

# #Somando todos os elementos da lista
total_vendas = sum(vendas)
print(f'Total de vendas: R${total_vendas:.2f}')

# #Tamanho da lista
quantidade_vendas = len(vendas)
print(f'Quantidade de vendas: {quantidade_vendas}')

# #Maior valor, menor valor (max e min)
maior_valor = max(vendas)
menor_valor = min(vendas)
# print(f'Maior venda: R${maior_valor:.2f} | Menor venda: R${menor_valor:.2f}' )

# #printando direto
print(f'Maior venda: R${max(vendas):.2f} | Menor venda: R${min(vendas):.2f}' )

# #Pegar um elemento da lista 
print(f'Venda 01: R${vendas[0]:.2f} | Venda 03: R${vendas[2]:.2f} | Venda 05: R${vendas[4]:.2f}')

# #LISTA DE PRODUTOS
produtos = ['iphone', 'airpods', 'ipad', 'macbook']

#Verificando se elemento esta dentro da lista
print('apple watch' in produtos)
#Retorna 'false' pois o produto não existe na lista

#Buscando um elemento com a entrada do usuario
pesqusa_produto = input('Qual produto deseja encontrar: ')
pesqusa_produto = pesqusa_produto.lower()
print(pesqusa_produto in produtos)

#Adicionar um item na lista
produtos.append('apple watch')
print(produtos)

#Remover um item na lista
produtos.remove('ipad') #Eu passo o elemento que quero remover
print(produtos)

produtos.pop(1) #Eu passo o indice do item que quero remover
print(produtos)

#Editar um item na lista
preco_produtos = [1000, 1500, 980]
preco_produtos[0] = 4500
print(preco_produtos)

#Contar quantas vezes aparece um item na lista
print(produtos.count('macbook'))

#Ordenar uma lista
preco_produtos.sort() #Ordem crescente
print(preco_produtos)

preco_produtos.sort(reverse=True) #Ordem decrescente
print(preco_produtos)
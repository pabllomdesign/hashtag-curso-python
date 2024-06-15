#Manipulação de stings
faturamento = 1520
custo = 700
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento
margem = round(margem_lucro,(2))

#Formatacao do print usando f{string}
print(f'O faturamento foi de: {faturamento}, custo de {custo} e o lucro de {lucro}')

#Transformando o texto em maiúscula ou minuscula
email_cliente = 'emailqualquer@gmail.com'

#Maiúscula
email_cliente= email_cliente.upper()
print(email_cliente)

#Minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

#Find permite encontrar um elemento dentro do texto
#Caso ele não encontre o elemento informado é retornado -1
print(email_cliente.find('@'))

#Len retorna o tamanho do texto
print(len(email_cliente))

#Retorna um elemento do texto
print(email_cliente[13])
#Retorna '@'

#Retornar até o indice 14
print(email_cliente[:13])
#Retorna 'emailqualquer'

#Retornar do indice 13 até o indice 23
print(email_cliente[13:23])
#Retorna '@gmail.com'

#Trocar um pedaco do texto
novo_email = email_cliente.replace('@gmail.com', '@hotmail.com')
print(novo_email)

#Capitalizando um texto
nome = 'pabllo martins'
#Capitalize pega a primeira letra e deixa em maiúscula
print(nome.capitalize()) 
#Retorna 'Pabllo martins'

#Title deixa a primeira letra de cada palavra em maiúscula
print(nome.title())
#Retorna 'Pabllo Martins'

#Formatando de texto númerico
print(f'O faturamento: R${faturamento:.2f}, custo: R${custo:.2f}, lucro: R${lucro:.2f} e margem de lucro: {margem:.0%}' )
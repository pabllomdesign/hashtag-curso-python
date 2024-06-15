#Pegar o servidor de um email
email_cliente = 'pabllomoliveiraa@gmail.com'
posicao_arroba = email_cliente.find('@')
servidor = email_cliente[posicao_arroba +1:]
print(f'O provedor de e-mail é:{servidor}')



#Pegar o primeiro nome e o sobrenome
nome_cliente = "Pabllo Martins"
posicao_espaco = nome_cliente.find(' ')
nome = nome_cliente[:posicao_espaco]
sobrenome = nome_cliente[posicao_espaco +1:]
print(f'Primeiro nome: {nome}')
print(f'Sobrenome: {sobrenome}')

#Caso o nome tenha mais espaços
nome_completo = "Paulo Ricardo Oliveira Martins"
nomes = nome_completo.split()
primeiro_nome= nomes[0]
sobrenome_completo = nomes[-1]
print(primeiro_nome, sobrenome_completo)



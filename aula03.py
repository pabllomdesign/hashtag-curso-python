#Sobre Inputs

#Entrada de dados do usuario
input('Digite seu nome: ')

#Armazenando a entrada em uma variável
nome = input('Digite seu nome: ')
email = input('Digite seu e-mail:' )
print(f'Seja bem-vindo {nome}, verifique o email {email} para validar as informações.')

#Convertendo inputs, pois ele sempre retorna uma string e caso precise usar numeros.
idade = int(input('Qual a sua idade: ')) #Converter para um numero inteiro
altura = float(input('Qual a sua altura: ')) #Converte para um numero flutuante
print('Dados de cadastro:')
print(f'Nome: {nome}\ne-mail: {email}\nIdade:{idade}\nAltura:{altura}')

faturamento = 1000 #Variável tipo int = inteiro | Número
custo = 700.32 #Variável tipo float = Decimal | Números flutuantes
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento
print('Relatório de Faturamento:') # Tipo string | Textos
print('-'*30)
print(f'O faturamento foi de R${faturamento:.2f}\nO custo foi de R${custo:.2f}\nO lucro de R${lucro:.2f}') 
print(f'A margem de lucro foi de: {margem_lucro:.2f}')
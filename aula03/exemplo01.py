# Atividade - Aumento Salarial

#Entrada
salario = float(input('Informe o salário: '))
percentual = float(input('Informe a porcentagem de aumento: '))

#Processamento
percentual = percentual / 100
valor_aumento = salario * percentual
salario_reajustado = salario + valor_aumento

#Saida
print(f'\nSalario atual: R$ {salario}')
print(f'Valor do aumento: {valor_aumento}')
print(f'Salario com reajuste: R$ {salario_reajustado}')
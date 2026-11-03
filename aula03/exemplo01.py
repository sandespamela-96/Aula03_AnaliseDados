# Atividade - Aumento Salarial

#Entrada
salario = float(input('Informe o salário: '))

#Processamento
valor_aumento = salario * 0.15
salario_reajustado = salario + valor_aumento

#Saida
print(f'\nSalario atual: R$ {salario}')
print(f'Valor do aumento: {valor_aumento}')
print(f'Salario com reajuste: R$ {salario_reajustado}')
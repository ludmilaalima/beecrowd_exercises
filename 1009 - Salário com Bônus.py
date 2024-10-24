nome = input()
salario = float(input())
total_vendas = float(input())

vendas = total_vendas * 15.00 / 100.00

novo_salario = salario + vendas

print(f"TOTAL = R$ {novo_salario:.2f}")
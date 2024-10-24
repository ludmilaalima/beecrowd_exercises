codigo1, num_peca1, valor_uni1 = input().split(" ")

#12 1 5.30

codigo1 = int(codigo1)
num_peca1 = int(num_peca1)
valor_uni1 = float(valor_uni1)

codigo2, num_peca2, valor_uni2 = input().split(" ")

codigo2 = int(codigo2)
num_peca2 = int(num_peca2)
valor_uni2 = float(valor_uni2)

total1 = num_peca1 * valor_uni1
total2 = num_peca2 * valor_uni2


print(f"VALOR A PAGAR: R$ {total1 + total2 :.2f}")
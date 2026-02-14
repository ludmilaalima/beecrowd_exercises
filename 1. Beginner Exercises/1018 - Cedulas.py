banknote = int(input())

banknote_total = banknote

banknote100 = 0
banknote50 = 0
banknote20 = 0
banknote10 = 0
banknote5 = 0
banknote2 = 0
banknote1 = 0

while banknote!=0:
    while banknote >= 100:
        banknote100+=1
        banknote = banknote - 100
    while banknote >=50:
        banknote50+=1
        banknote = banknote - 50
    while banknote >= 20:
        banknote20 += 1
        banknote = banknote - 20
    while banknote >= 10:
        banknote10 += 1
        banknote = banknote - 10
    while banknote >= 5:
        banknote5 += 1
        banknote = banknote - 5
    while banknote >= 2:
        banknote2 += 1
        banknote = banknote - 2
    while banknote >= 1:
        banknote1 += 1
        banknote = banknote - 1

print(banknote_total)
print(
    f'{banknote100} nota(s) de R$ 100,00'
)
print(
    f'{banknote50} nota(s) de R$ 50,00'
)
print(
    f'{banknote20} nota(s) de R$ 20,00'
)
print(
    f'{banknote10} nota(s) de R$ 10,00'
)
print(
    f'{banknote5} nota(s) de R$ 5,00'
)
print(
    f'{banknote2} nota(s) de R$ 2,00'
)
print(
    f'{banknote1} nota(s) de R$ 1,00'
)

value1, value2, value3 = input().split()

a = int(value1)
b = int(value2)
c = int(value3)

highest_number_a_b = (a + b + abs(a-b))/2
highest_number = (highest_number_a_b + c + abs(highest_number_a_b-c))/2


print(f"{highest_number:.0f} eh o maior")
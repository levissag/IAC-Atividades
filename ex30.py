numeros = []
i=0

while i<5:
    num = int(input("Digite um numero "))
    numeros.append(num)
    i = i+1

print(f'\nO maior numero é {max(numeros)} e o menor é {min(numeros)}')


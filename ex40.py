nomes = ['joao', 'marcos', 'andre', 'levi', 'luizao']
alturas = []
cod_matriculas = []
maior = 0
menor = 10

for i in nomes:
    altura = float(input(f'Informe a altura da pessoa {i}: '))
    cod_matricula = input(f'Informe o cod_matricula da pessoa {i}: ')
    alturas.append(altura)
    cod_matriculas.append(cod_matricula)
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

maiorPos = alturas.index(maior)
menorPos = alturas.index(menor)

print(f'Altura do maior aluno> Nome: {nomes.__getitem__(maiorPos)} | Altura: {alturas.__getitem__(maiorPos)} | Cod: {cod_matriculas.__getitem__(maiorPos)}')
print(f'Altura do menor aluno> Nome: {nomes.__getitem__(menorPos)} | Altura: {alturas.__getitem__(menorPos)} | Cod: {cod_matriculas.__getitem__(menorPos)}')



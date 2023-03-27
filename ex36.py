nomes = ['joao', 'marcos', 'andre', 'levi', 'luizao', 'davison', 'fernando', 'anderson', 'wesley', 'fulano']
idades = []
nacionalidades = []
qtd_apto = 0

for i in nomes:
    idade = int(input(f'Informe a idade da pessoa {i}: '))
    nacionalidade = input(f'Informe a nacionalidade da pessoa {i}: ')
    idades.append(idade)
    nacionalidades.append(nacionalidade)
    if idade > 16 and nacionalidade == 'br':
        qtd_apto += 1

print(f'\n{nomes}')
print(f'{nacionalidades}')
print(f'{idades}')
print(f'Aptos para votacao: {qtd_apto} pessoas')


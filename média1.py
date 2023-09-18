notas = []
contador = 1

while contador <= 4:
    notas.append(float(input(f'informe a {contador} nota: ')))
    contador += 1

nota_maior = max(notas)
nota_menor = min(notas)
media = sum(notas) / len(notas)

print(f'a maior nota é {nota_maior} e a menor nota é {nota_menor} e a média final é {media}')
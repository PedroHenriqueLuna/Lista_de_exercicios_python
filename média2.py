notas = []
contador = 1

while contador <= 4:
    notas.append(float(input(f'informe a {contador} nota: ')))
    contador += 1

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado por média")
else:
    notas.append(float(input("informe a nota da prova final: ")))
    media = sum(notas) / len(notas)
    print(f'Sua média final é {media}')

    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
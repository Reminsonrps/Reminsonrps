primeira_nota = float(input("Digite um número: "))
segunda_nota = float(input("Digite um número: "))
media = (primeira_nota + segunda_nota) / 2
               
print(f'primeira nota :{primeira_nota}. segunda nota: {segunda_nota}. média: {media}')
               
if media >= 7:
  print("Aprovado")
else:
  print("Reprovado")

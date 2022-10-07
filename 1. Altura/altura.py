#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

sexo = int(input('Escolha: 1 - Masculino / 2 - Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

if sexo == 1:
	peso_ideal = (72.7*h) - 58
else:
	peso_ideal = (62.1*h) - 44.7

print("Peso ideal: ", peso_ideal)

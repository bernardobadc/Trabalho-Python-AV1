#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

kg = float(input("Digite o número de KG de peixes:"))
excesso = 0

if kg <= 50:
    print("Peso dentro do limite estabelecido!")
else:
    excesso = kg - 50
    print("Excesso =", excesso)
    multa = excesso * 4
    print("Valor da multa: R$", multa)








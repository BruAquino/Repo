#1 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

Valor = int(input("Insira um valor negativo ou positivo. "))
if Valor > 0:
  print("O seu valor é positivo.")

elif Valor < 0:
  print("O seu valor é negativo.")

else:
  print("O seu valor é zero.")

#2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Sexo = (input("Insira o seu genero com F (Feminino) ou M (Masculino): "))
if Sexo == "F" or Sexo == "f":
  print("O seu sexo é feminino.")

elif Sexo == "M" or Sexo == "m":
  print("O seu sexo é masculino.")

else:
  print("Sexo invalido.")

#3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("digite uma letra: ")

if letra == ("a" or "e" or "i" or "o" or "u"):
  print ("A letra digitada é uma vogal")

else:
  print ("A letra digitada é uma consoante")

#4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez

nota = float(input("Diga a sua nota: "))

if nota == 7 or nota > 7 and nota < 10:
  print ("Aprovado")

elif nota == 10:
  print ("Aprovado com Distinção")

else:
  print ("Reprovado")

#5 - Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("digite um número: "))
num2 = int(input("digite um número: "))
num3 = int(input("digite um número: "))

maiorNum = max(num1, num2, num3)

print("O maior número é:",maiorNum)

#6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

num4 = int(input("digite um número: "))
num5 = int(input("digite um número: "))
num6 = int(input("digite um número: "))


maiorNum1 = max(num4, num5, num6)
menorNum = min(num4, num5, num6)

print("O maior número é:",maiorNum1,". E o menor número é:", menorNum)

#7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produtoUm = int(input("Digite um valor: "))
produtoDois = int(input("Digite um valor: "))
produtoTres = int(input("Digite um valor: "))

menorValor = min(produtoUm, produtoDois, produtoTres)

print("O menor valor é:", menorValor)

#8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("DIgite um número: "))
numero2 = int(input("DIgite um número: "))
numero3 = int(input("DIgite um número: "))

if numero1 < numero2 and numero2 < numero3:
  print(numero3, numero2, numero1)

if numero1 < numero3 and numero3 < numero2:
  print(numero2, numero3, numero1)

if numero2 < numero1 and numero1 < numero3:
  print(numero2, numero1, numero3)

if numero3 < numero1 and numero1 < numero2:
  print(numero3, numero1, numero2)

if numero3 < numero2 and numero2 < numero1:
  print(numero3, numero2, numero1)

if numero2 < numero3 and numero3 < numero1:
  print(numero2, numero3, numero1)

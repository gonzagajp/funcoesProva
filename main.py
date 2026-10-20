from funcoes_do_aluno import eh_impar
from funcoes_do_aluno import eh_par
from funcoes_do_aluno import calcula_dobro
from funcoes_do_aluno import calcula_media
from funcoes_do_aluno import calcular_salario

#Se é par ou impar
num = int(input("Digite um número: "))
eh_par
eh_impar

if eh_par (num):
    print("É par")
else:
    print("É impar")

#Calcular dobro

numero = float(input("Digite um numero: "))
resultado = calcula_dobro(numero)
calcula_dobro

print("O dobro do  valor é: ", resultado)

#Calcular media

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
resultado = calcula_media (nota1, nota2, nota3)
print(resultado)

#Calcular salario

horas_trabalhadas = float(input("Qual a quantidade de horas trabalhadas? "))
valor_por_hora = float(input("Qual o valor da hora trabalhada? "))
salario = calcular_salario (horas_trabalhadas, valor_por_hora)
print(salario)






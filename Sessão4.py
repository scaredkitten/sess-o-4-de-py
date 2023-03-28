
"""
1:
numero = int(input('Escreva um número real: '))

print(numero)

2:
numero = float(input('Escreva um número real: '))

print(numero)

3:
numero_1 = int(input('Escreva seu primeiro inteiro: '))

numero_2 = int(input('Escreva seu segundo inteiro: '))

numero_3 = int(input('Escreva seu terceiro inteiro: '))

numero_final = numero_1 + numero_2 + numero_3

print(numero_final)

4:
numero = float(input('Digite seu numero real: '))

numero_final = numero * numero

print(f'O quadrado do seu número é : {numero_final}')

5:
numero = str(input('Escreva seu número real: '))

float_numero = float(numero)

print(type(float_numero))
print('{:.6f}'.format(float_numero)[6])

Ou

numero = float(input('Escreva um número real: '))

numero_final = numero / 5

print (numero_final)

6:
temp_celsius = float(input('Escreva sua temperatura em Celsius: '))

temp_fahrenheit = temp_celsius * (9.0/5.0) +32

print(f'Sua temperatura em Fahrenheit seria: {temp_fahrenheit} graus')

7:
tempf = float(input('Digite sua temperatura em Fahrenheit: '))
tempc = 5.0 * (tempf - 32) / 9.0

print(f'Sua temperatura em Celsius seria: {tempc}graus')

8:
tempk = float(input('Digite sua temperatura em Kelvin: '))

tempc = tempk - 273.16

print(f'Sua temperatura em Celsius seria: {tempc}')

9:
tempc = float(input('Digite sua temperatura em Celsius: '))

tempk = tempc + 273.15

print(f'Sua temperatura em Kelvin é {tempk} graus')
10:
velocidade_KMH = float(input('Digite sua velocidade em KM/h: '))

velocidade_MS = velocidade_KMH / 3.6

print(f'Sua velocidade em m/s é :{velocidade_MS}')

11:
velocidade_ms = float(input('Digite sua velocidade em m/s: '))

velocidade_kmh = velocidade_ms * 3.6

print(f'Sua velocidade em KM/h é: {velocidade_kmh}')

12:
milhas = float(input('Digite sua distância em milhas: '))

km = 1.61 * milhas

print(f'Sua distância em km é {km}')

13:
km = float(input('Digite sua distância em KM/h: '))

milhas = km/1.61

print(f'Sua distância em milhas é {milhas}')

14:
import math

graus = float(input('Digite seu ângulo em graus: '))

radianos = graus * math.pi/180 

print(f'Seu ângulo em radianos é: {radianos}')

15:
import math

radianos = float(input('Digite seu ângulo em radiano: '))

graus = radianos * 180/math.pi 

print(f'Seu ângulo em radianos é: {graus}')

16:
pol = float(input('Digite seu comprimento em polegadas: '))

cm = pol * 2.54

print(f'Seu comprimento em cm é {cm}')

17:
cm = float(input('Digite seu comprimento em cm: '))

pol = cm/2.54

print(f'Seu comprimento em polegadas é {pol}')

18:
m_3 = float(input('Digite seu valor em m³: '))

litro = 1000 * m_3

print(f'Seu valor em litros é: {litro}')
19:
litro = float(input('Digite seu valor em litros: '))

m_3 = litro/1000 

print(f'Seu valor em m³ é: {m_3}')
20:
kg = float(input('Digite o valor da massa em KG: '))

libras = kg/0.45
print(f'Sua massa em Libras é {libras}')
21:
libras = float(input('Digite o valor da massa em Libras: '))
kilo = libras * 0.45
print(f'O valor da massa em KG é {kilo}')
22:
jardas = float(input('Digite o comprimento em Jardas: '))
metros = 0.91 * jardas
print (f'O valor do comprimento em metros é: {metros}')
23: 
metros = float(input('Digite seu comprimento em metros: '))
jardas = metros/0.91
print(f'Seu comprimento em jardas é {jardas}')
24:
m2 = float(input('Digite sua área em m²: '))
acre= m2 * 0.000247
print(f'Sua área em Acres é de: {acre}')
25:
acre = float(input('Digite sua área em acres: '))
m2 = acre * 4048.58 
print(f'Sua área em m² é de: {m2}')
26:
m2 = float(input('Digite sua área em m²: '))
hec = m2 * 0.0001
print(f'Sua área em hectares é de: {hec}')
27:
hec = float(input('Digite sua área em hectares: '))
m2 = hec *10_000
print(f'Sua área em m² é de {m2}')
28:
valor1 = int(input('digite seu primeiro valor: '))
valor2 = int(input('digite seu segundo valor: '))
valor3 = int(input('digite seu terceiro valor: '))

quadrado1 = valor1 * valor1
quadrado2 = valor2 * valor2
quadrado3 = valor3 * valor3

valor_final = quadrado1 + quadrado2 + quadrado3

print(f'A soma dos quadrados dos valores digitados é de: {valor_final}')
29:
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))
nota4 = float(input('Digite a quarta nota:'))

nota_somada = nota1 + nota2 + nota3 + nota4
nota_final  = nota_somada/4

print(f'A média do aluno foi de {nota_final}')
30:
real = float(input('Digite o valor em Real: '))
cotacao = float (input('Digite a cotação do Dólar: '))
dolar = real * cotacao
print (f'{dolar}')

31:
num = int(input('Digite um número: '))
print (f'{num + 1}')
print (f'{num - 1}')
32:
num = int(input('Digite um inteiro: '))
triplo = num * 3 + 1
dobro1 = num * 2
dobro_final = dobro1 - 1
num_final = dobro_final + triplo

print(f'{num_final}')
33:
lado = float(input('Digite o valor do Lado de um quadrado: '))
area = lado * lado

print(f'{area}')
34:
raio = float(input('Digite o raio do círculo desejado: '))
raio2 = raio * raio
area = 3.141592 * raio2

print(f'A área de seu círculo la ele tem: {area}')
35:
import math

cateto_a = int(input('Digite o valor do cateto a: '))
cateto_b = int(input('Digite o valor do cateto b: '))
cateto_a2 = cateto_a * cateto_a
cateto_b2 = cateto_b * cateto_b
hipotenusa = math.sqrt (cateto_a2 + cateto_b2)
print(f'Sua hipotenusa é {hipotenusa}')
36:
altura = float(input('Digite a altura: '))
raio = float(input('Digite o valor do raio: '))
raio2 = raio * raio
volume = 3.141592 * raio2 * altura
print(f'O valor do volume é de : {volume}')
37:
preco = float(input('Informe o valor do produto: '))
preco_final = preco * 0.88
print(f'O valor do produto com desconto é de {preco_final}')
38:
salario = float(input('Digite o salário do funcionário: '))
salario_final = salario * 1.25
print(f'O novo salário do funcionário será de {salario_final}')
39:
premio = 780_000.00
porcentagem1 = 0.46
porcentagem2 = 0.32
ganhador1 = 780_000.00 * porcentagem1
ganhador2 = 780_000.00 * porcentagem2
ganhador3 = 780_000.00 - ganhador1 - ganhador2

print(ganhador1, ganhador2, ganhador3)
40:
dias = int(input('Digite o número de dias que o encanador trabalhou: '))
valor = dias * 30
valor_final = valor *0.92
print(f'O valor que o encanador receberá sem desconto do imposto e renda é de {valor}')
print(f'O valor que o encanador receberá com o desconto do imposto de renda é de {valor_final}')
41:
valor_trabalho = int(input('Digite o valor pago à cada hora de trabalho: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))

valor = horas_trabalhadas * valor_trabalho
valor_final = valor *1.1
print(valor, valor_final)
42:
salario = float(input('Digite o salário do funcionário: '))
salario_grat = salario *0.05
salario_imposto = salario * 0.07
salario_final = salario + salario_grat - salario_imposto

print(f'O salário recebido pelo funcionário foi de {salario_final}')
43:
valor_total = float(input('Digite o valor total: '))
desconto = valor_total * 0.1
total_pagar = valor_total * 1.1
parcela = valor_total / 3
comissão_a_vista = total_pagar * 0.05
comissão_parcelada = valor_total * 0.05

print(valor_total, total_pagar, parcela, comissão_a_vista, comissão_parcelada, desconto)
44:
altura_degrau = float(input ('Informe a altura do degrau: '))
altura_alvo = float(input('Informe a altura que você deseja alcançar: '))
quantidade_degraus = altura_degrau * altura_alvo

print(f'A quantidade de degraus que você precisará é de: {quantidade_degraus}')
45:
letra_maiuscula = input("Digite uma letra maiúscula: ")
letra_minuscula = chr(ord(letra_maiuscula) + 32)
print("A letra minúscula correspondente é:", letra_minuscula)
46:
num = int(input('Digite um número positivo de 3 dígitos: '))
if num <100:
    print('Número menor que 100')
    num = int(input('Digite um número positivo de 3 dígitos: '))
if num >999:
    print ('Número maior que 999')
    num = int(input('Digite um número positivo de 3 dígitos: '))
if num <=999 and num >=100:
    num_str = str(num)
    print(num_str[::-1])
47:
    num = int(input('Digite um número de 1000 a 9999: '))

if num < 1000 or num > 9999:
    print('VALOR INVÁLIDO!!!')
    
else:
    num_str = str(num)
    for digit in num_str:
        print(digit)
48:
segundos = int(input('Digite um valor sem segundos: '))

minutos = segundos / 60 

horas = minutos / 60

print(f'Seu valor em segundos é: {segundos}\n')
print(f'Seu valor em minutos é de : {minutos}\n')
print(f'Seu valor em horas é de: {horas}')
49:
import datetime

hora_inicio = int(input('Digite a hora de início (0-23): '))
minuto_inicio = int(input('Digite o minuto de início (0-59): ')) 
segundo_inicio = int(input('Digite o segundo de início (0-59): '))

duracao_segundos = int(input('Digite a duração em segundos: '))

inicio = datetime.datetime(2023, 3, 16, hora_inicio, minuto_inicio, segundo_inicio)

termino = inicio + datetime.timedelta (seconds = duracao_segundos)

print('O horário de término é:', termino.time())
50:
idade = int(input('Fale a sua idade: '))
aniversario = str(input('Você já fez aniversário esse ano? Responda com "Sim" ou "Não" '))
ano_atual = 2023
nascimento = ano_atual - idade

if aniversario == 'Sim':
    nascimento = nascimento
elif aniversario == 'Não':
    nascimento = nascimento - 1 

print (f'Você nasceu em {nascimento}.')
51:
import math

x = int(input('Informe o valor de seu "x": '))
y = int(input('Informe o valor de seu "y": '))

d = math.sqrt(x**2 + y**2)

print(f'Sua distância é de {d}')
52:
valor_apostador1 = float(input("Digite o valor investido pelo apostador 1: "))
valor_apostador2 = float(input("Digite o valor investido pelo apostador 2: "))
valor_apostador3 = float(input("Digite o valor investido pelo apostador 3: "))

valor_premio = float(input("Digite o valor do prêmio: "))

total_investido = valor_apostador1 + valor_apostador2 + valor_apostador3

proporcao_apostador1 = valor_apostador1 / total_investido
proporcao_apostador2 = valor_apostador2 / total_investido
proporcao_apostador3 = valor_apostador3 / total_investido

valor_ganho_apostador1 = valor_premio * proporcao_apostador1
valor_ganho_apostador2 = valor_premio * proporcao_apostador2
valor_ganho_apostador3 = valor_premio * proporcao_apostador3

print("O apostador 1 ganhou R$", valor_ganho_apostador1)
print("O apostador 2 ganhou R$", valor_ganho_apostador2)
print("O apostador 3 ganhou R$", valor_ganho_apostador3)
53: 
comprimento = int(input('Informe  o comprimento do terreno: '))
largura = int(input('Informe a largura do terreno: '))
preco_tela = int(input('Informe o preço do metro de tela: '))

perimetro = comprimento * 2 + largura * 2
preco_total = perimetro * preco_tela

print (preco_total)

"""











#Variáveis

a = 10
# esta variavel eh do tipo inteiro (int)
b = 1.2
# esta variavel e do tipo real (float)
c = "Ola mundo"
'''esta variavel e do tipo string (conjunto de caracteres)
Digite type(a) e veja o resultado'''

#Entrada e saída de dados
nome = input("Digite o nome do usuario: ")

#Conversão de variáveis
idade = int(input("Digite a idade da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))
#ou pode converter uma variavel para string
num = 123321
identidade = str(num)

#Saída de dados
print("Ola mundo")
idade = int(input("Digite a idade da pessoa: "))
print("A idade da pessoa e", idade)
altura = float(input("Digite a altura da pessoa: "))
print("A idade da pessoa e", idade,"e a altura e",altura)

#Operações com string
a = "5"
b = "5"
c = a + b
print (c)

#Comandos de decisão
num = int(input("Digite um numero: "))
if num >= 10:
    print("Numero e maior que 10")
else:
    print("Numero e menor que 10")

#Comando de repetição
for i in range(0,5):
    print("Numero", i)

i = 0
while i < 5:
    print("Numero", i)
    i = i + 1

#Funções
def somar(num_1,num_2):
    soma = num_1 + num_2
    return (print(soma))
x = int(input("Digite um numero: "))
y = int(input("Digite um outro numero: "))
somar(x,y)

#Vetores
#declaracao de um vetor vazio
vet = []
#inserindo numeros no vetor usando funcao append
vet.append(2)
vet.append(4)
vet.append(6)
vet.append(8)
print(vet)
print(vet[2])
#e possivel inserir strings em vetores
vet2 = []
vet2.append("Joao") 
vet2.append("Maria")
vet2.append("Jose")
print(vet2)
#Usando comando de repeticao
vet3 = []
for i in range(0,5):
    vet3.append(i)

#Strings
#declaracao de uma string
frase = "Ola mundo"
print(frase[2])
#declaracao de um vetor
vet = []
vet.append("Joao")
vet.append("Maria")
print(vet)
#substituindo uma string da primeira posicao do vetor
vet[0] = 'A'
#substituindo um caracter da primeira posicao de uma string. Isso retornara um erro
frase[0] = 'A'

#declaracao de uma string
frase = "Ola mundo"
#substituindo o caracter "O" pelo caracter "A"
print(frase.replace("O","A"))
print(frase)
#a frase nao sera alterada, o metodo retorna um valor, porem, nao altera a variavel
nome = "IEEE"
#podemos passar a quantidade de substituicoes
nome.replace("E","A",2)	


#Matrizes
matriz = []
for i in range(0,3):
    matriz.append([1,2,3])
print(matriz)

matriz = []
for i in range(0,3):
    matriz.append([1,2,3])
print(matriz[0][0])
matriz[0][0] = 2
print(matriz)

matriz = []
for i in range(0,3):
    aux = []
    for j in range(0,3):
        num = int(input("Digite um numero a ser inserido na matriz: "))
        aux.append(num)
    matriz.append(aux)
print(matriz)


#Manipulação de arquivos
f = open("palavras.txt","r")
for linha in f:
    print(linha)	
f.close()

f = open("palavras.txt","r")
nomes = []
for linha in f:
    campos = linha.split(" ")
    nomes.append(campos[0])	
f.close()
print(nomes)

f = open("palavras.txt","r")
anos = []
for linha in f:
    campos = linha.split(" ")
    anos.append(campos[1].strip())	
f.close()
print(anos)

arq = open("Meu_arquivo.txt","w")
arq.write("Olá mundo")
arq.write("Meu nome é marcelo")
arq.write("Sou estudante da UERJ\n")
arq.write("\tFaço parte do Ramo Estudantil IEEE UERJ.\n")
arq.close()

#Math
import math
#calcula o fatorial
print(math.factorial(5))
#calcula o log
print(math.log(2,2))
#calcula o numero 4 elevado ao quadrado
print(math.pow(4,2))
#calcula a raiz quadrada
print(math.sqrt(16))
#calcula o seno, cosseno e os arcos
print(math.cos(90))
print(math.sin(90))
print(math.acos(-0.448))
print(math.asin(0.893))
#converta o angulo de radianos em graus.
print(math.degrees(math.pi/2))
#converta o angulo de graus em radianos
print(math.radians(180))

#Random
import random
print ( random . randint (5 ,15))

#Time
import time
#retorma hora atual
print(time.localtime())
#inicia contagem
antes = time.time()
#aguarda dois segundos
time.sleep(2)
#finaliza tempo de contagem
depois = time.time()
tempo = depois-antes
print(tempo)
#imprimi somente com duas casas decimais
print("%.2f" %tempo)

#OS
import os
#abrindo a calculadora
os.system("calc")
#abrindo prompt de comando
os.system("cmd.exe")
#criando uma pasta
os.system("mkdir CapacitacaoPython")
#armazenando saida do comando em um arquivo
os.system("ipconfig" +  " > saida.txt")

#Matplotlib
import matplotlib.pyplot as plt
#defindo valores que ficarao no eixo x e no eixo y
plt.plot([1,2,3,4],[1,4,9,16])
plt.title("Primeiro grafico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show()


import time

#Biblioteca para retornar um número inteiro aleatório
from random import randint as rd
sorteado = rd(-100, 100) #Sorteia um número de -100 a 100
# print(sorteado)

#criando uma lista de números inteiros aleatórios
lista = [rd(1,6) for i in range(10)]
lista2 = [x for x in range(1,11) ]
lista3 = ["Rolocompressor!!!" for c in range(1,5)]

# print(lista)
# print(lista2)
# print(lista3)

#lista par
par = [i for i in range(10) if i % 2 == 0]
# print(par)

#Povoando uma lista com 'input'
# listaUsuario = [input("Digite um número: ")for p in range(2)]
# print(listaUsuario)

# ultilizando o método split
# nome = 'Mickey Mouse'
# print(nome)
# print(nome.split())
# print(nome)

# #aplicando o "split" com input
# notas = [n for n in input("Notas: ").split()]
# print(notas)

# #numeros dentro de uma lista em float
# notas2 = [ float(n) for n in input("Notas: ").split()]
# print(notas2)

listaMista = [17, 70.5, 'adriano time ruim', True]
# print(listaMista)

veiculos1 = ["carro", "bicicleta", "moto"]
# print("Veiculos 1: ", veiculos1)

# veiculos2 = veiculos1
# del veiculos1[0]
# print("veiculos 2: ", veiculos2)

#copiando todo o conteudo de uma lista para outra
veiculos2 = veiculos1[:]
del veiculos1[2]
# print("Veiculos 1:", veiculos1)
# print("Veiculos 2:", veiculos2)

veiculos3 = veiculos2[0:1]
# print(veiculos3)

veiculos4 = veiculos2[0:-1]
# print(veiculos4)

veiculos5 = veiculos2[-1:1]
# print(veiculos5)

#outra maneira
my_list = ["A","B","C","D","E","F"]
print(my_list)

new_list = my_list[:3]
print(new_list)

new_list_fim = my_list[3:]
print(new_list_fim)

del my_list[1:3]
print(my_list)
del my_list[:]
print(my_list)








































































time.sleep(1)
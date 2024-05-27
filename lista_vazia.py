import time

my_list = [] #lista vazia

for c in range(5):
    my_list.append(c + 1)

print(my_list)

#lista vazia 02
my_list2 = [] #lista02 vaiza
for c in range(5):
    my_list2.insert(0, c + 1)

print(my_list2)

#terceira lista
my_list3 = [10, 1, 8, 3, 5]

total = 0

for c in range(len(my_list3)):
    total = total + my_list3[c]

print(total)

total = 0

for c in my_list3:
    total += c

print(total) 

#reordenando a lista manualmente
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]
#print(my_list3)

#reordenando sem saber o tamanho da lista
tamanhoLista = len(my_list3)

for c in range(tamanhoLista // 2):
    my_list3[c], my_list3[tamanhoLista - c - 1] = my_list3[tamanhoLista - c - 1], my_list3[c]

print(my_list3)

time.sleep(1)
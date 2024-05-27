lista_beatles = []

lista_beatles.append("John Lennon")
lista_beatles.append("Paul McCartney")
lista_beatles.append("George Harrison")

print(lista_beatles)

for c in range(2):
    lista_beatles.append(str(input("Digite um nome: ")))

print(lista_beatles)
    
for c in range(2):
    del lista_beatles [-1]

print(lista_beatles)

lista_beatles.insert(0, "Ringo Starr")

print(lista_beatles)

("o fabuloso", len(beatles))
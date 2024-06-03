import time

#função
def somar():
    n1 = int(input("digite o primerio número da adição: "))
    n2 = int(input("digite o segundo número: "))
    print(n1 + n2)

# somar()



def somar2(n1, n2):
    soma = n1 + n2
    return soma

# print("Soma 2:", somar2(22,20))

def somar3(n1, n2):
    return n1 + n2
# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))
# print(somar3(10, 15))

# print(somar3(n2 = 12, n1 = 5))

def somar4(n1 = 0, n2 = 0):
    return n1 + n2

# print(somar4(50,25))
# print(somar4())


def somar5(n1,n2=0):
    return n1 + n2
print(somar5(50, 25))
print(somar5(10))
print(somar5(n2 = 51, n1 = 12))

def somar6(n1,n2):
    if n1 == 1:
        return True

print(somar6 (1,3))#true
print(somar6(13,3))#None
print(somar6(1,2) + 10)

time.sleep(1)
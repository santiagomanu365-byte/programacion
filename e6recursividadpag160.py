print("-------------------------------------------------------")
print("Complemento6: INVERTIR NÚMERO.")
print("-------------------------------------------------------")

aux = 0
aux2 = 0
print("Ingrese un número: ")
n = int( input())
while n > 0:
    aux = n % 10
    n = n // 10
    aux2 = aux2 * 10 + aux
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El número invertido será:", aux2)
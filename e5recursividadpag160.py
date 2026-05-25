print("-------------------------------------------------------")
print("Complemento5: CALCULAR SUMA DE SERIE 2.")
print("-------------------------------------------------------")

S = 0

print ("Ingrese número de términos:")
N = int( input())

for x in range(1, N+1):
    if x % 2 == 0:
        S = S - (1/x)
    else:
        S = S + (1/x)

print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("La suma será:", S)
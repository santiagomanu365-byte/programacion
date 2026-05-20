
print("-------------------------------------------------------")
print("Ejercicio6: DETERMINAR VALOR Y RANGO MAYOR A 300.")
print("-------------------------------------------------------")

A1 = 1
A2 = 0
An = A1 + (2 * A2)
cont = 0
while An < 300:
    A2 = A1
    A1 = An
    An = A1 + (2 * A2)
    cont = cont + 1

print("\nSALIDA: ")
print("-------------------------------------------------------")

print("El rango es:", cont, "y el resultado es:", An)

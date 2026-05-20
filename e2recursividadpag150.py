
print("-------------------------------------------------------")
print("Ejercicio2: Calcula la suma de divisores.")
print("-------------------------------------------------------")
#Entradas
print("Introduce un número, y para acabar uno negativo:")
numero = int( input("Núm: "))
while numero > 0 :
   suma = 0
   for i in range(1,numero+1):
      if numero % i == 0 :
         suma = suma + i
   #Salida
   print("\nSALIDA: ")
   print("----------------------------------------------------")
   print("La suma de los divisores del número es:", suma, "\n")
   print("Introduce un número, y para acabar uno negativo:")
   numero = int(input("Núm: "))
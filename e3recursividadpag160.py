print("-------------------------------------------------------")
print("Complemento3: CUBO DE UN NÚMERO PRIMO.")
print("-------------------------------------------------------")

b = 2

for i in range(1, 29):
	co = 0
	# comprobar si b es primo
	for a in range(2, int(b**0.5) + 1):
		if b % a == 0:
			co = co + 1
			break
	if co == 0:
		print("El cubo de", b, " es: ", b**3)
	b = b + 1
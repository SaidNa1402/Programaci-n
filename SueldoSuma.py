def suma_primeros_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

sueldo = int(input("Ingresa el sueldo del empleado: "))
suma = suma_primeros_n(sueldo)

print(f"La suma de los términos desde 1 hasta {sueldo} es {suma}")

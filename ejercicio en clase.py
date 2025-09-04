import sys

entero = int(input("Ingrese un número entero: "))
real = float(input("Ingrese un número real (decimal): "))
cadena = input("Ingrese una cadena de texto: ")

print(f"\nVariable entero: valor = {entero}, tipo = {type(entero)}, bytes reservados = {sys.getsizeof(entero)}")
print(f"Variable real: valor = {real}, tipo = {type(real)}, bytes reservados = {sys.getsizeof(real)}")
print(f"Variable cadena: valor = '{cadena}', tipo = {type(cadena)}, bytes reservados = {sys.getsizeof(cadena)}")

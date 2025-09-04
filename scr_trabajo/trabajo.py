#Manuel Santiago Garzon Rodriguez

# MEMORIA ESTÁTICA (inmutable)

cursos = ("Matemáticas", "Programación", "Bases de Datos", "Redes")  
estudiante = "Juan Pérez" 


# MEMORIA DINÁMICA (mutable)

calificaciones = []  


# FUNCIONES


def agregar_calificacion(nota):
    """Agrega una nota a la lista de calificaciones."""
    calificaciones.append(nota)

def modificar_calificacion(indice, nueva_nota):
    """Modifica una nota existente en la lista."""
    if 0 <= indice < len(calificaciones):
        calificaciones[indice] = nueva_nota
    else:
        print("Índice inválido.")

def eliminar_calificacion(indice):
    """Elimina una nota de la lista."""
    if 0 <= indice < len(calificaciones):
        calificaciones.pop(indice)
    else:
        print("Índice inválido.")

def calcular_promedio():
    """Calcula el promedio de las calificaciones."""
    if calificaciones:
        return sum(calificaciones) / len(calificaciones)
    else:
        return 0

# ----------------------------
# PROGRAMA PRINCIPAL
# ----------------------------
print(f"Estudiante: {estudiante}")
print("Cursos:", cursos)


agregar_calificacion(4.0)
agregar_calificacion(3.5)
agregar_calificacion(5.0)

print("Notas actuales:", calificaciones)

modificar_calificacion(1, 4.2)
print("Notas después de modificar:", calificaciones)

eliminar_calificacion(0)
print("Notas después de eliminar:", calificaciones)

promedio = calcular_promedio()
print(f"Promedio final de {estudiante}: {promedio:.2f}")


# OPCIONAL: Diccionario curso → nota

informe = dict(zip(cursos, calificaciones))
print("Diccionario:", informe)
tu_puntaje = float(input("Ingresa tu puntaje (entre 0.0 y 1.0): "))

if tu_puntaje < 0.0 or tu_puntaje > 1.0:
    print("Error: La puntuación debe estar entre 0.0 y 1.0.")
elif tu_puntaje >= 0.9:
    print("Excelente")
elif tu_puntaje >= 0.8:
    print("Muy bien")
elif tu_puntaje >= 0.7:
    print("Bien")
elif tu_puntaje >= 0.6:
    print("Regular")
else:
    print("Reprobado")

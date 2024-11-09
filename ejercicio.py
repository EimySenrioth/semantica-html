#ex1
while True:
    try:
        horas_trabajadas = float(input("¿Cuántas horas has trabajado? "))
        pago_hora = 10
        pago_hora_extra = pago_hora * 1.5
        if horas_trabajadas <= 40:
            salario = horas_trabajadas * pago_hora
        else:
            salario = 40 * pago_hora + ((horas_trabajadas - 40) * pago_hora_extra)
        
        print(f"Tu salario es: {salario}")
        break  # Sale del bucle si la conversión es exitosa
    except ValueError:
        print("Error: ingrese un valor numérico válido.")
#ex 2
tu_puntaje = float(input("Ingresa tu puntaje ente 0.0 y 1.0"))

if tu_puntaje < 0.0 or tu_puntaje > 1.0:
    print("Error: el puntaje debe estar entre 0.0 y 1.0")

elif tu_puntaje >= 0.9:
    print("Excelente")
elif tu_puntaje >= 0.8:
    print("Muy bien")
elif tu_puntaje >= 0.7:
    print("Bien")
elif tu_puntaje >= 0.6:
    print("Regular")
else:
    print ("Reprobado")
        
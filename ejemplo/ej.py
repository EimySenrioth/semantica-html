try:
    # Solicita al usuario que ingrese las horas trabajadas
    horas_trabajadas = float(input("¿Cuántas horas has trabajado? "))
    
    # Tarifa horaria y tarifa para horas extra
    pago_hora = 10
    pago_hora_extra = pago_hora * 1.5

    # Cálculo del salario con pago extra para horas mayores a 40
    if horas_trabajadas <= 40:
        salario = horas_trabajadas * pago_hora
    else:
        salario = 40 * pago_hora + (horas_trabajadas - 40) * pago_hora_extra

    # Muestra el salario calculado
    print(f"Tu salario es: {salario} pesos")

except ValueError:
    # Captura de error en caso de entrada no numérica
    print("Error: por favor, ingrese un valor numérico válido.")
12
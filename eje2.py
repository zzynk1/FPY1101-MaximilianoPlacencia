def registrar_usuario():
    print("--- Registro de Usuario ---")
    nombre=input("Nombre del alumno: ").strip()
    carrera=input("Carrera: ").strip()
    return {"nombre": nombre, "carrera": carrera}

def registrar_libro():
    print("--- Registro de Libro ---")
    libro=input("Titulo del libro: ").strip()
    while True:
        try:
            dias=int(input("Dias de prestamo solicitados: "))
            if dias > 0:
                return{"libro": libro, "dias": dias}
            print("Los dias deben ser mayores a 0")
        except ValueError:
            print("Ingrese un numero entero valido")

def generar_resumen(usuario, libro_info):
    print("=== REPORTE FINAL DE RESERVA ===")
    print(f"Alumno: {usuario['nombre']}")
    print(f"Carrera: {usuario['carrera']}")
    print(f"Libro: {libro_info['libro']}")
    print(f"Dias: {libro_info['dias']} dias")

    if libro_info['dias'] > 14:
        print("El prestamo supera los 14 dias permitidos")
        print("Recuerde que podria aplicar sanciones o multas")
    else:
        print("Prestamo dentro del plazo")

def main_biblioteca():
    print("=== SISTEMA DE RESERVAS DE BIBLIOTECA ===")
    usuario=registrar_usuario()
    libro_info=registrar_libro()
    generar_resumen(usuario, libro_info)

if __name__ == "__main__":
    main_biblioteca()
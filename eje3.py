def validar_nota():
    while True:
        try:
            nota=float(input("Ingrese nota (1.0 a 7.0): "))
            if 1.0 <= nota <= 7.0:
                return nota
            print("La nota debe estar en el rango de 1.0 a 7.0")
        except ValueError:
            print("Ingrese un numero valido")

def calcular_promedio(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def mostrar_estado(alumno, promedio):
    print("=== ESTADO ACADEMICO ===")
    print(f"Alumno: {alumno}")
    print(f"Promedio final: {promedio:.1f}")
    if promedio >= 4.0:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

def menu_erp():
    alumno=""
    notas=[]

    while True:
        print("=== MINI ERP ACADEMICO ===")
        print("1. Registrar alumno y notas")
        print("2. Mostrar estado academico (reporte)")
        print("3. Salir")

        opcion=input("Seleccione una opcion (1-3): ").strip()

        if opcion == "1":
            alumno=input("Nombre del alumno: ").strip()
            notas=[]
            while True:
                try:
                    cant_notas=int(input(f"¿Cuantas notas desea registrar para {alumno}?: "))
                    if cant_notas > 0:
                        break
                    print("Debe registrar al menos 1 nota")
                except ValueError:
                    print("Ingrese un numero entero valido")
            
            for i in range(1, cant_notas + 1):
                print(f"Nota {i}:")
                nota_validada=validar_nota()
                notas.append(nota_validada)

        elif opcion == "2":
            if not alumno:
                print("Primero debe registrar un alumno y sus notas")
            else:
                promedio=calcular_promedio(notas)
                mostrar_estado(alumno, promedio)
        elif opcion == "3":
            print("Saliendo del sistema academico...")
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion del 1 al 3")

if __name__ == "__main__":
    menu_erp()
    
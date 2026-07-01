def validar_temperatura():
    while True:
        try:
            temp=float(input("Ingrese una temperatura en grados celcius: "))
            return temp
        except ValueError:
            print("Por favor, ingrese un numero valido")

def calcular_promedio(temperaturas):
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)

def obtener_alerta(promedio):
    if promedio < 10:
        return "Alerta: Clima frio"
    elif 10 <= promedio <= 25:
        return "Alerta: Clima templado"
    else:
        return "Alerta: Clima calido"
    
def main_temperaturas():
    print("=== SISTEMA DE GESTION DE TEMPERATURAS ===")
    temperaturas=[]
    for i in range(1, 6):
        print(f"Temperatura {i}/5:")
        temp=validar_temperatura()
        temperaturas.append(temp)

    promedio=calcular_promedio(temperaturas)
    alerta=obtener_alerta(promedio)

    print("=== REPORTE FINAL DE TEMPERATURAS ===")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Promedio de temperaturas: {promedio:.2f} °C")
    print(f"Estado: {alerta}")

if __name__ == "__main__":
    main_temperaturas()
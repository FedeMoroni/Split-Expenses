nombreYgasto = input("Inserte nombre y gasto: (formato: nombre,gasto)")
dic = {}

while len(nombreYgasto.split(",")) == 2:
    nombre, gasto = nombreYgasto.strip().split(",")
    gasto = float(gasto)
    dic[nombre] = gasto
    nombreYgasto = input("Inserte nombre y gasto: (formato: nombre,gasto)")

n = len(dic.keys())
total = sum(dic.values())
cadaUno = total/n

cobran = []
deben = []

for nombre, gasto in dic.items():
    if gasto > cadaUno:
        cobran.append((nombre, gasto - cadaUno)) 
    elif gasto < cadaUno:
        deben.append((nombre, cadaUno - gasto))   

opcion = input("\n¿Sugerir quien transfiere a quien, o imprimir cuanto debe cada uno y los que deben le transfieren a uno que cobre, y el que cobra le transfiere lo suyo a los que cobran? [opcion A/opcion B] (formato: A)")

if opcion.strip().upper() == "A":
    print("\nPagos sugeridos:")
    i, j = 0, 0
    while i < len(deben) and j < len(cobran):
        deudor, debe_monto = deben[i]
        acreedor, cobra_monto = cobran[j]

        pago = min(debe_monto, cobra_monto)
        print(f"{deudor} tiene que pagar ${pago:.2f} a {acreedor}")
        
        deben[i] = (deudor, debe_monto - pago)
        cobran[j] = (acreedor, cobra_monto - pago)
        if deben[i][1] == 0:
            i += 1
        if cobran[j][1] == 0:
            j += 1

else:
    print("\nResumen de deudas y cobros:")
    print("Quienes deben:")
    for nombre, monto in deben:
        print(f"{nombre} tiene que pagar ${monto:.2f}")
    print("\nQuienes cobran:")
    for nombre, monto in cobran:
        print(f"{nombre} tiene que cobrar ${monto:.2f}")

print(f"\nEl gasto total por persona es ${cadaUno}")
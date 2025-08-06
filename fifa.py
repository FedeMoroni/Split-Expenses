import math
import matplotlib.pyplot as plt

plt.ion()  # Modo interactivo ON

n = int(input("Cantidad de equipos:"))
equipos = []

for i in range(n):
    nombre = input(f"Nombre del equipo {i+1}:")
    equipos.append({"nombre_equipo": nombre, "pts": 0, "pj": 0, "gf": 0, "gc": 0})

def imprimirEquipos():
    impresion = ""
    for equipo in equipos:
        impresion = impresion + equipo["nombre_equipo"] + "\n"
    return f"Quienes juegan ahora?: (formato: equipo1 equipo2)\nLos equipos son:\n{impresion}"

match = input(imprimirEquipos())
fig, ax = plt.subplots(figsize=(8, 2 + n * 0.3))  # Crear figura una sola vez

while match != "fin":
    match = match.strip().split(" ")
    nombreEquipo1 = match[0]
    nombreEquipo2 = match[1]
    estadoEquipo1 = input(f"Como le fue al {nombreEquipo1}? (formato: pts gf gc)").strip().split(" ")
    estadoEquipo2 = []

    if int(estadoEquipo1[0]) == 3:
        estadoEquipo2.append(0)
    elif int(estadoEquipo1[0]) == 1:
        estadoEquipo2.append(1)
    else:
        estadoEquipo2.append(3)
    estadoEquipo2.append(int(estadoEquipo1[2]))
    estadoEquipo2.append(int(estadoEquipo1[1]))

    for equipo in equipos:
        if equipo["nombre_equipo"] == nombreEquipo1:
            equipo["pts"] += int(estadoEquipo1[0])
            equipo["pj"] += 1
            equipo["gf"] += int(estadoEquipo1[1])
            equipo["gc"] += int(estadoEquipo1[2])
        elif equipo["nombre_equipo"] == nombreEquipo2:
            equipo["pts"] += int(estadoEquipo2[0])
            equipo["pj"] += 1
            equipo["gf"] += int(estadoEquipo2[1])
            equipo["gc"] += int(estadoEquipo2[2])

    # Ordenar equipos por puntos y goles a favor (descendente)
    equipos_ordenados = sorted(
        equipos,
        key=lambda x: (x["pts"], x["gf"]),
        reverse=True
    )

    # Actualizar tabla en la misma ventana
    ax.clear()
    ax.axis('off')

    columnas = ["Equipo", "Pts", "PJ", "GF", "GC"]
    datos = [
        [equipo['nombre_equipo'], equipo['pts'], equipo['pj'], equipo['gf'], equipo['gc']]
        for equipo in equipos_ordenados
    ]

    tabla = ax.table(cellText=datos, colLabels=columnas, loc='center', cellLoc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1, 1.5)

    ax.set_title('Tabla de puntuación')
    fig.canvas.draw()
    fig.canvas.flush_events()

    match = input(imprimirEquipos())

plt.ioff()  # Desactivar modo interactivo
plt.show()  # Mantener la ventana abierta al final
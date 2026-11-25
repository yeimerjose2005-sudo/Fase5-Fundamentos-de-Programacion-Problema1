
# Problema 1 - Fase 5
# Clasificacion del compromiso de sesiones de clientes

# Matriz con los datos de las sesiones
sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 6],
    [104, 200, 5],
    [105, 50, 10]
]

# Funcion para clasificar el compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Generar el informe de resultados
print("INFORME DE COMPROMISO DE CLIENTES")
print("---------------------------------")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente, "- Compromiso:", clasificacion)

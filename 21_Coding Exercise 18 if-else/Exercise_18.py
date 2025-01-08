# Objetivo
# Programa un "Creador de Recomendaciones de Películas" utilizando la estructura de control de flujo if-else en Python

# Solución
def recomendar_película(genero, edad):
    if genero == "acción" and edad >= 13:
        return "Deadpool"
        print(f'Teniendo en cuenta tu edad ({edad}) y tu género favorito ({genero}), te recomiendo la siguiente película: {película_recomendada}')
    elif genero == "acción" and edad < 13:
        return "Regreso al futuro"
        print(f'Teniendo en cuenta tu edad ({edad}) y tu género favorito ({genero}), te recomiendo la siguiente película: {película_recomendada}')
    elif genero == "comedia":
        return "Aterriza como puedas"
    else:
        return "Explorar otros géneros"

genero_favorito = "thriller"
edad_usuario = 12
película_recomendada = recomendar_película(genero_favorito, edad_usuario)

print(f'Teniendo en cuenta tu edad ({edad_usuario}) y tu género favorito ({genero_favorito}), te recomiendo la siguiente película: {película_recomendada}')



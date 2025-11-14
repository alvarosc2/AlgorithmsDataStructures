import random

def volado():
    return random.choice(['Sol', 'Aguila'])

players = [
    {'name': 'Alvaro Silva', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': True},
    {'name': 'Roberto Galvan', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Carlos Martinez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Diana Lopez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Eduardo Ramirez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Fernanda Torres', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Gabriel Morales', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Helena Castro', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ignacio Flores', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Julia Mendez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Kevin Ortiz', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Laura Sanchez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Miguel Reyes', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Natalia Cruz', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Oscar Hernandez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Patricia Vargas', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Quintin Delgado', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Rosa Jimenez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Santiago Ruiz', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Teresa Navarro', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ulises Pena', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Valeria Romero', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'William Guerrero', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ximena Soto', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Yolanda Medina', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Zachary Aguilar', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Andrea Rojas', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Bruno Vega', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Claudia Ibarra', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Daniel Paz', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Elena Duran', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Felipe Campos', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Gloria Salazar', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Hector Fuentes', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Isabel Vasquez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Jorge Acosta', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Karina Rios', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Luis Mendoza', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Monica Carrillo', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Nicolas Cabrera', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Olivia Nunez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Pablo Estrada', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ramona Calderon', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Sergio Lara', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Tatiana Perez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Umberto Guzman', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Veronica Luna', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Walter Mejia', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Xiomara Arias', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Yasmin Benitez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Zack Paredes', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Adriana Molina', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Benito Cano', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Carmen Villarreal', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Diego Serrano', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Elisa Ramos', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Francisco Blanco', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Graciela Dominguez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Hugo Vidal', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Irene Camacho', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Javier Santos', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Karla Trejo', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Lorenzo Avila', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Mariana Gil', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Norberto Leon', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ofelia Herrera', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Pedro Cortes', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Regina Silva', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Salvador Espinoza', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Tania Juarez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Uriel Pacheco', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Victoria Ochoa', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Winston Salas', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Xander Mora', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Yesenia Rivera', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Zara Mejia', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Alberto Gomez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Beatriz Castillo', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Cesar Marin', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Dolores Rubio', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Emilio Ponce', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Fabiola Cardenas', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Gonzalo Barrera', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Hortensia Montoya', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ivan Galindo', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Jazmin Velasco', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Kristian Deleon', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Lorena Alarcon', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Marcos Alvarado', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Noemi Cervantes', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Omar Sandoval', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Pilar Valenzuela', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Rigoberto Valdez', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Silvia Zamora', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Tomas Zavala', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False},
    {'name': 'Ursula Arellano', 'coins': 100, 'wins': 0, 'loses': 0, 'is_sol': False}
]

# let's shuffle the array of players
random.shuffle(players)

for i in range(0, 100):
    result = volado()

    if result == 'Sol' and players[0]['is_sol'] == True:
        players[0]['wins'] += 1
        players[0]['coins'] += 1

        players[1]['loses'] += 1
        players[1]['coins'] -= 1
    elif result == 'Aguila' and players[0]['is_sol'] == True:
        players[0]['loses'] += 1
        players[0]['coins'] -= 1

        players[1]['wins'] += 1
        players[1]['coins'] += 1

print(players)
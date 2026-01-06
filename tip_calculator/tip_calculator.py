def tip_calculator(total_bill: float, tip_percentage: float, people_to_split: int) -> float:
    return round((total_bill / people_to_split) * (1 + tip_percentage / 100), 2)

def get_positive_float(prompt: str) -> float:
    """Solicita un número decimal positivo hasta que sea válido."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: El valor debe ser mayor a cero. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")


def get_positive_integer(prompt: str) -> int:
    """Solicita un número entero positivo mayor a cero hasta que sea válido."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Debe ingresar un número entero mayor a cero. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
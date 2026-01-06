from tip_calculator import tip_calculator, get_positive_float, get_positive_integer

def main():
    print("Welcome to the tip calculator!")
    
    # Validar entrada de la cuenta total (float positivo)
    total_bill = get_positive_float("What was the total bill? $ ")
    
    # Validar entrada del porcentaje de propina (float positivo)
    tip_percentage = get_positive_float("How much tip would you like to give? 10, 12, 15, or 20? ")
    
    # Validar entrada de personas (entero positivo mayor a cero)
    people_to_split = get_positive_integer("How many people to split the bill? ")
    
    # Calcular y mostrar resultado
    amount_per_person = tip_calculator(total_bill, tip_percentage, people_to_split)
    print(f"Each person should pay: $ {amount_per_person}")

if __name__ == "__main__":
    main()
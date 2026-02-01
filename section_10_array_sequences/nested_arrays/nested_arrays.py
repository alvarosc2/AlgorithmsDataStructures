fruits = ["Strawberries", "Nectarines", "Apples", "Grales", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celeries", "Potatoes"]

dirty_dozen = [fruits, vegetables]

for array in dirty_dozen:
    for item in array:
        print(f"{item:13}", end="")
    print()  # New line after each row
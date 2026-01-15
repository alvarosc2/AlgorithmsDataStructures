tax_rate = 0.16
size_price: float = 0.0
pepperoni_price: float = 0.0
extra_cheese_price: float = 0.0
total_before_taxes: float = 0.0

print("Welcome to the Python Pizza Delivery program!")

while True:
    size: str = input("What size of pizza do you want? S, M or L: ")

    if size == "S" or size == "s":
        size_price = 15.0
        total_before_taxes = size_price
        break
    elif size == "M" or size == "m":
        size_price = 20.0
        total_before_taxes = size_price
        break
    elif size == "L" or size == "l":
        size_price = 25.0
        total_before_taxes = size_price
        break
    else:
        print("Error: invalid option for pizza size. Try again.")

while True:
    pepperoni: str = input("Do you want pepperoni on your pizza? Y or N: ")

    if pepperoni == "Y" or pepperoni == "y":
        if size == "S" or size == "s":
            pepperoni_price = 2.0
            total_before_taxes += pepperoni_price
            break
        elif size == "M" or size == "m" or size == "L" or size == "l":
            pepperoni_price = 3.0
            total_before_taxes  += pepperoni_price
            break
        else:
            print("Error: The only options for pricing pepperoni are S, M or L")
    elif pepperoni == "N" or pepperoni == "n":
        total_before_taxes += 0.0
        break
    else:
        print("Error: invalid option for pepperoni. Try again.")

while True:
    extra_cheese: str = input("Do you want extra cheese? Y or N: ")

    if extra_cheese == "Y" or extra_cheese == "y":
        extra_cheese_price = 1.0
        total_before_taxes += extra_cheese_price
        break
    elif extra_cheese == "N" or extra_cheese == "n":
        total_before_taxes += 0.0
        break
    else:
        print("Error: invalid option for extra cheese. Try again.")

taxes: float = total_before_taxes * tax_rate
total_to_pay: float = round(total_before_taxes * (1 + tax_rate),)

print("Your order: ")
print("")
print(f"Pizza size: {size_price}")
if pepperoni_price > 0.0:
    print(f"Pepperoni: {pepperoni_price}")

if extra_cheese_price > 0.0:
    print(f"Extra cheese: {extra_cheese_price}")

print(f"Total b/taxes: {total_before_taxes}")
print(f"Taxes ({tax_rate * 100}%): {taxes}")
print(f"Total to pay: {total_to_pay}")

tax_rate = 0.16
size_price: float = 0.0
pepperoni_price: float = 0.0
extra_cheese_price: float = 0.0
total_before_taxes: float = 0.0

print("Welcome to the Python Pizza Delivery program!")
size: str = input("What size of pizza do you want? S, M or L: ")
pepperoni: str = input("Do you want pepperoni on your pizza? Y or N")
extra_cheese: str = input("Do you want extra cheese? Y or N")

if size == "S":
    size_price = 15.0
    total_before_taxes = size_price
elif size == "M":
    size_price = 20.0
    total_before_taxes = size_price
elif size == "L":
    size_price = 25.0
    total_before_taxes = size_price
else:
    print("Error: size option not available")

if pepperoni == "Y":
    if size == "S":
        pepperoni_price = 2.0
        total_before_taxes += pepperoni_price
    elif size == "M" or size == "L":
        pepperoni_price = 3.0
        total_before_taxes  += pepperoni_price
    else:
        print("Error: The only options for pricing pepperoni are S, M or L")
elif pepperoni == "N":
    total_before_taxes += 0.0
else:
    print("Error: pepperoni option not available")

if extra_cheese == "Y":
    extra_cheese_price = 1.0
    total_before_taxes += extra_cheese_price

taxes: float = total_before_taxes * tax_rate
total_to_pay: float = total_before_taxes * (1 + tax_rate)

print("Your order: ")
print("")
print(f"Pizza size: {size_price}")
if pepperoni_price > 0.0:
    print(f"Pepperoni: {pepperoni_price}")
if extra_cheese_price > 0.0:
    print(f"Extra cheese: {extra_cheese_price}")

print(f"Total b/taxes: {total_before_taxes}")
print(f"Taxes: {taxes}")
print(f"Tota to pay: {total_to_pay}")

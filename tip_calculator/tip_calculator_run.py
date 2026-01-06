from tip_calculator import tip_calculator

total_bill: float = 0.0
tip_percentage: float = 0.0
people_to_split: int = 1
amount_per_person: float = 0.0

print("Welcome to the tip calculator!")
print("What was the total bill?")
total_bill = float(input("$"))

print("How much tip would you like to give?")
tip_percentage = float(input("10, 12, 15, or 20?"))

people_to_split = int(input("How many people to split the bill?"))

amount_per_person = tip_calculator(total_bill, tip_percentage, people_to_split)

print(f"Each person should pay {amount_per_person}")
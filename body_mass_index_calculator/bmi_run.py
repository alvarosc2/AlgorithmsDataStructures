bmi: float = 0.0

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("normal weight")
elif bmi >= 25.0:
    print("overweight")
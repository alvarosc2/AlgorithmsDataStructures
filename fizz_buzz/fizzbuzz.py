for i in range(1, 101):
    # first we must evaluate if the given number is divisible by 3 AND by 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Next we evalute if the number is divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # Next we evaluate if the number is divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # Any other number is printed as it is
    else:
        print(i)
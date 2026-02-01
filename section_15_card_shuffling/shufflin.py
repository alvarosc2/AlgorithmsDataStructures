import random

def swap(a, b):
    return (b, a)

def shuffle(arr):
    for i in range(0, len(deck)):
        s = random.randint(0, len(deck) - 1)
        arr[i], arr[s] = swap(arr[i], arr[s])

    return arr
    
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

deck = shuffle(deck)

print(deck)



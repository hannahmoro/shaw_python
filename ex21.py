def add(a, b): #defines add function with arguments a and b
    print(f"ADDING {a} + {b}") #message declaring self
    return a + b #returns the sum of a and b

def subtract(a, b): #ditto but now subtracts
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b): #ditto but multiply
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b): #ditto but division
    print(f"DIVIDE {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

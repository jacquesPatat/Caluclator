from art import logo 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        print("Available operations: " + " ".join(operations.keys()))
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if cont == "y":
            num1 = result
        else:
            should_continue = False
            calculator()  # Restart calculator

calculator()

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
    "/": divide
}

def calculator():
    should_continue = True

    print(logo)
    first_number = float(input("What is the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        mathematical_operator = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))

        calculation_function = operations[mathematical_operator]
        result = calculation_function(first_number, second_number)

        print(f"{first_number} {mathematical_operator} {second_number} = {result}")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if should_continue == "y":
            first_number = result
        else:
            should_continue = False
            print("\n" * 100)
            calculator()

calculator()

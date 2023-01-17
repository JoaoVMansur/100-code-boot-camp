from art import logo


def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mult(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    }
def calculator():
    
    print(logo)
    
    n1 = float(input("What's the first number?: "))
    for symbols in operations:
        print(symbols)

    again = "y"
    while again == "y":
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")
        
        again = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation : ")
        if again == "y":
            n1 = result
        elif again == "n":
            calculator()

calculator()
        



    
    
    
    
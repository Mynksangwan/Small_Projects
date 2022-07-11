from art import logo
import os
clear = lambda: os.system('clear')


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide 
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for operator in operations: 
        print(operator)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick a operation: ")

        num2 = float(input("What's the next number?: "))
        # passing operation_symbol through dictionary operations to get value like add , subtract , multiply or divide 
        # and passing arguments for that predefined functions above in code 

        result = operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        cond = input(f"Type 'y' to continue working with {result} or type 'n' to exit: ")

        if cond == 'y':
            num1 = result
        else : 
            should_continue = False
            clear()
            calculator()

calculator()
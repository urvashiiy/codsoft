                                                    #Program for simple calculator
def add(x,y):               #define add function
    return x + y

def substract(x,y):         #define substract function
    return x - y

def multiply(x,y):          #define multiply function
    return x * y

def divide(x,y):            #define divide function
    if y == 0:
     return  "cannot divide by zero"
    return x / y


while True:
    print("Options:")                                   #giving the option to the user to choose operation
    print("Enter 'add' for addition")
    print("Enter 'substract' for substraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    choice = input("Enter your choice:")

    if choice == "exit":
        break
    
    if choice in("add","substract","multiply","divide"):
        num1 = float(input("enter first number: "))                   #take input from user
        num2 = float(input("enter second number: "))

        if choice == "add":                                             
            print("Result:",add(num1,num2))
        elif choice == "substract":
            print("Result:",substract(num1,num2))
        elif choice == "multiply":
            print("Result:",multiply(num1,num2))
        elif choice == "divide":
            print("Result:",divide(num1,num2))

        else:
            print("invalid input")
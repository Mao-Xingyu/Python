

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while True:
    # take input from the user
    choice = input("Select operation \n1.Add\n2.Subtract\n3.Multiply\n4.Divide ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        match choice:
            case "1":
                print(num1, "+", num2, "=", add(num1, num2))
            case "2":
                print(num1, "-", num2, "=", subtract(num1, num2))
            case "3":
                print(num1, "*", num2, "=", multiply(num1, num2))
            case "4":
                print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        NC = input("Let's do next calculation? (yes/no): ")
        if (NC == "no") or (NC == "No") or (NC == "NO"):
          break
    else:
        print("Invalid Input")
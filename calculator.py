
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exp(num1, num2):
    return num1 ** num2

def sqrt(num1):
    return math.sqrt(num1)

def cubeRoot(num1):
    return num1 ** (1/3)

def mod(num1, num2):
    return num1 % num2

print("You will need to choose the operation:\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Power\n"
        "6. Square Root\n"
        "7. Cube Root\n"
        "8. Modulo\n")

try:
    select = int(input("Please select operations:"))


except:
    print('Error. Please select one operation. Your output should be 1, 2, 3, 4, 5, 6, 7 or 8.')

else:
    try:
        import math
        number1 = input("Enter first number: ")

        if number1 == "pi":
            number1 = math.pi
        elif number1 == "e":
            number1 = math.e
        else:
            number1 = float(number1)


            if select == 6:
                print("The square root of", number1, "is", sqrt(number1))
            elif select == 7:
                print("The cube root of", number1, "is", cubeRoot(number1))
            else:
                number2 = input("Enter second number: ")

                if number2 == "pi":
                    number2 = math.pi
                elif number2 == "e":
                    number2 = math.e
                else:
                    number2 = float(number2)

    except:
        print('Error. Please enter numbers')

    else:
        if select == 1:
            print(number1, "+", number2, "=",
                            add(number1, number2))

        elif select == 2:
            print(number1, "-", number2, "=",
                            subtract(number1, number2))

        elif select == 3:
            print(number1, "*", number2, "=",
                            multiply(number1, number2))

        elif select == 4:
            print(number1, "/", number2, "=",
                            divide(number1, number2))
        elif select == 5:
            print(number1, "**", number2, "=",
                            exp(number1, number2))
        elif select == 8:
            print(number1, "%", number2, "=",
                            mod(number1, number2))



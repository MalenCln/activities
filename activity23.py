def factorial(number):
    """ This function's purpose is to compute/calculate the factorial of any number given """
    fact = 1
    for x in range(number, 0, -1):
        fact *= x

    return fact

print(f"the factorial of 5 is {factorial(5)}")
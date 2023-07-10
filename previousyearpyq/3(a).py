
    
    
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = input("Enter a positive integer: ")
number = int(number)  # Convert the input to an integer

factorial = factorial_recursive(number)

print(f"The factorial of {number} is: {factorial}")

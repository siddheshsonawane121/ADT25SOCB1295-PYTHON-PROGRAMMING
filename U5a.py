try:
    num = int(input("Enter an integer number: "))
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

except ValueError as e:
    print("Error:", e)

else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")

finally:
    print("Program execution completed.")
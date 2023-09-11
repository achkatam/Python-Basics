age = int(input("Age:"))
print(age)  # If entered a string, it will throw an error

# To handle this error, we use try-except block
try:
    age = int(input("Age:"))
    income = 50000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value!")
    print("Please enter you age in numbers.")
except ZeroDivisionError:
    print("Age cannot be 0.")

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()


# compare two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is:", larger_number)





# same code other way
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2: larger_number = number1
else: larger_number = number2

print("The larger number is:", larger_number)




# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number is the largest one.
largest_number = number1

# We check if the second number is larger than current largest_number and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)



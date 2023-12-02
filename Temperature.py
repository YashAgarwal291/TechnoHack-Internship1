def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
# print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")

a=int(input("enter the number "))

fahrenheit_temperature = celsius_to_fahrenheit(a)
print(f"{a} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")


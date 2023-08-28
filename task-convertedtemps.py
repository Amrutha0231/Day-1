temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit == 'C' or unit == 'c':
    converted_temperature = temperature * 9/5 + 32
    converted_unit = '°F'
elif unit == 'F' or unit == 'f':
    converted_temperature = (temperature - 32) * 5/9
    converted_unit = '°C'
else:
    print("Invalid unit entered!")
    exit()

print(f"Converted temperature: {converted_temperature:.2f}{converted_unit}")

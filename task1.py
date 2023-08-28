input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in input_numbers.split()]

even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

duplicate_numbers = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate_numbers:
        duplicate_numbers.append(number)
    else:
        continue

print(duplicate_numbers)
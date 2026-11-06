word = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels: {}".format(count))
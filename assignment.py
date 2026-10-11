

print("Numbers divisible by 7 but not by 3:")
numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print(",".join(numbers))



print("\nConvert list of characters into a string:")
characters = ["C", "o", "d", "i", "n", "g"]
result = "".join(characters)

print(result)


print("\nDictionary of numbers and their squares:")
n = int(input("Enter a number: "))
square_dict = {}

for i in range(1, n + 1):
    square_dict[i] = i * i

print(square_dict)

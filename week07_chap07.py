numbers = list()

for i in range(0, 11):
    numbers.append(i)

print(numbers)
reverse_numbers = numbers[::-1]
print(reverse_numbers)
print(numbers)
numbers.reverse()
print(numbers)

numbers.append(-11)
print(numbers)

numbers.insert(5, 99)
print(numbers)
numbers.insert(-2, 55)
print(numbers)

numbers *= 2 # list multiplication
print(numbers)

numbers1 = list()

for i in range(0, 5):
    numbers1.append(i)

print(numbers1)
numbers3 = numbers1 + numbers
print(numbers1)
print(numbers3)
numbers1.extend(numbers)
print(numbers1)
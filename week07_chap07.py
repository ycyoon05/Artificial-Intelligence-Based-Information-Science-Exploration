numbers = list()

for i in range(0, 11):
    numbers.append(i)

print(numbers)
print(numbers[-2])
print(numbers[-11], numbers[0])

odd_numbers = numbers[1::2]
even_numbers = numbers[0::2]
reverse_odd_numbers = numbers[-2::-2]
reverse_numbers = numbers[::-1]

print(odd_numbers)
print(even_numbers)
print(reverse_odd_numbers)
print(reverse_numbers)
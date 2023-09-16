print(bool(None))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(0))

#vowels = "aeiou"
vowels = ['a', 'e', 'i', 'o', 'u']
letter = input("input alphabet letter: ")
if letter in vowels:
    print(f"{letter} is vowel~")
else:
    print(f"{letter} is no a vowel!")

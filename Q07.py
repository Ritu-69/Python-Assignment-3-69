text = input("Enter a string: ")
alphabets = 0
digits = 0
special_chars = 0

for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special_chars)

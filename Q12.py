text = input("Enter a string: ")
char = input("Enter the character to find: ")

first = text.find(char)
last = text.rfind(char)

if first != -1:
    print(f"First occurrence index: {first}")
    print(f"Last occurrence index: {last}")
else:
    print(f"'{char}' was not found in the string.")

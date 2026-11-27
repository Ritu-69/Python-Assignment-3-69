text = input("Enter a string: ")
char = input("Enter the character to check: ")

if text.startswith(char) and text.endswith(char):
    print(f"Yes, the string starts and ends with '{char}'.")
else:
    print(f"No, the string does not start and end with '{char}'.")

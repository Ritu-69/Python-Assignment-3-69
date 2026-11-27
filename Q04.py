text = input("Enter a string: ")
reversed_text = ""

# Loop through each character and prepend it to the new string
for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

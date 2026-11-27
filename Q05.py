text = input("Enter a string: ")
# Convert to lowercase to make the check case-insensitive
clean_text = text.lower()
reversed_text = ""

for char in clean_text:
    reversed_text = char + reversed_text

if clean_text == reversed_text:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")

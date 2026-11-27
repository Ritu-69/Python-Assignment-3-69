numbers = [10, 20, 40, 50]

element = int(input("Enter the element to insert: "))
position = int(input("Enter the index position: "))

numbers.insert(position, element)
print("Updated list:", numbers)

my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

element = int(input("Enter the element to remove: "))
if element in my_list:
    my_list.remove(element)
    print("List after removal:", my_list)
else:
    print("Element not found in the list.")

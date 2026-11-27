my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

index = int(input("Enter the index to delete: "))
if 0 <= index < len(my_list):
    removed_item = my_list.pop(index)
    print("Removed element:", removed_item)
    print("Updated list:", my_list)
else:
    print("Invalid index.")

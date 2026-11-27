# Creating a tuple with duplicate values
numbers = (10, 20, 30, 20, 40, 20, 50)

# Element to search for
target = 20

# Using count() method
occurrences = numbers.count(target)

print(f"The element {target} appears {occurrences} times in the tuple.")

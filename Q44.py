original = [1, 2, 3]

# Direct assignment (creates a reference to the same list)
assigned_list = original

# Using copy() (creates a separate shallow copy)
copied_list = original.copy()

# Modifying the original list
original.append(4)

print("Original list:", original)
print("Direct assignment (affected):", assigned_list)
print("Using copy() (unaffected):", copied_list)

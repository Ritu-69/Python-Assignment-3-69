my_list = [12, 45, 2, 41, 31, 10, 8, 6, 4]

# Remove duplicates and sort
unique_list = list(set(my_list))
unique_list.sort()

if len(unique_list) >= 2:
    print("Second-largest element:", unique_list[-2])
else:
    print("List does not have enough unique elements.")

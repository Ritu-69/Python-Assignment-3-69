numbers = [11, 22, 33, 44, 55, 66, 77]

even_count = 0
odd_count = 0

for num in numbers:
  if num % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

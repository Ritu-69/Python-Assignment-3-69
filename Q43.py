colors = ['red', 'green', 'blue', 'yellow']
target = 'blue'

if target in colors:
    index = colors.index(target)
    print(f"'{target}' is at index {index}.")
else:
    print(f"'{target}' is not in the list.")

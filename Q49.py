colors = ("red", "green", "blue")

# Demonstrating immutability (trying to modify raises a TypeError)
try:
    colors[1] = "yellow"
except TypeError as e:
    print("Immutability Error:", e)

# Creating a "modified" tuple by slicing and concatenating
modified_colors = colors[:1] + ("yellow",) + colors[2:]
print("Original tuple:", colors)
print("Modified tuple:", modified_colors)

# Write a program to sort (ascending order) a dictionary by value.

my_dict = {
    'a': 10,
    'b': 5,
    'c': 7,
    'd': 15
}
items = []
for key in my_dict:
    items.append((key, my_dict[key]))
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value

print(sorted_dict)

#A5_10. Write a program to display unique and duplicate elements of a tuple.

my_tuple = ()
n = int(input("Enter the no. of elements for the tuple: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    my_tuple+=(element,)

counts = {}
duplicates = set()
uniques = set()

for item in my_tuple:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item, count in counts.items():
    if count > 1:
        duplicates.add(item)
    else:
        uniques.add(item)

duplicates_list = sorted(list(duplicates))
uniques_list = sorted(list(uniques))

print("Unique elements:", uniques_list)
print("Duplicate elements:", duplicates_list)

#A5_11. Write a program to count the frequency of all the elements in a tuple.

my_tuple = ()
n = int(input("Enter the no. of elements for the tuple: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    my_tuple+=(element,)

counts = {}
for item in my_tuple:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item, count in counts.items():
    print(f"{item}: {count}")

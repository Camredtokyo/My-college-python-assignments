#A5_12. Write a program to find the distinct pair of numbers whose product is even from a tuple of
#integers.

my_tuple = ()
n = int(input("Enter the no. of elements for the tuple: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    my_tuple+=(element,)

pairs = set()
for i in range(len(my_tuple)):
    for j in range(i + 1, len(my_tuple)):
        if (my_tuple[i] * my_tuple[j]) % 2 == 0:
            pairs.add((my_tuple[i], my_tuple[j]))

for pair in pairs:
    print(pair)

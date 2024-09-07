#A5_04.Write a program to concatenate two lists using list comprehension.

l1= []
n = int(input("Enter the no. of elements for first list: "))
print("Enter the elements: ")
for i in range (n):
    element1 = int(input(f'Enter element no. {i+1} : '))
    l1.append(element1)
l2= []
m = int(input("Enter the no. of elements for second list: "))
print("Enter the elements: ")
for j in range (m):
    element2 = int(input(f'Enter element no. {j+1} : '))
    l2.append(element2)

l3=[i for i in l1] + [i for i in l2]
print(l3)

#A5_03. Write a program to find the union of two lists.


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

l3=[]
for element in l1:
    if element not in l3:
        l3.append(element)
for element in l2:
    if element not in l3:
        l3.append(element)

print(l3)

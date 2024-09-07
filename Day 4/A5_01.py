#A5_01. Write a program to find the maximum and minimum 
# of a list of numbers without using built-in functions.


l= []
n = int(input("Enter the no. of elements: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    l.append(element)

min=l[0]
max=l[0]
for i in range (len(l)):
    if (l[i]<min):
        min = l[i]
    if (l[i]>max):
        max = l[i]

print(f"Minimun element is {min}")
print(f"Maximum element is {max}")
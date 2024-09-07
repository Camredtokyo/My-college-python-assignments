#A5_08. Write a program to add elements in a tuple without using built-in functions.

original_tuple= ()
n = int(input("Enter the no. of elements for the original tuple: "))
print("Enter the elements: ")
for i in range (n):
    element1 = int(input(f'Enter element no. {i+1} : '))
    original_tuple+=(element1,)

additional_elements = (4, 5, 6)

additional_elements= ()
m = int(input("Enter the no. of elements for additional elements tuple: "))
print("Enter the elements: ")
for i in range (m):
    element2 = int(input(f'Enter element no. {i+1} : '))
    additional_elements+=(element2,)

new_tuple = original_tuple + additional_elements

print("The new tuple is:", new_tuple)

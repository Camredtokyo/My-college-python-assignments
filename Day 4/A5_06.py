#A5_06. Write a program to find the distinct pair of numbers whose product is
#odd from a list of integers.

l1= []
n = int(input("Enter the no. of elements for first list: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    l1.append(element)
    
odd_product = []

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] % 2 == 1 and l1[j] % 2 == 1:
            #product = l1[i] * l1[j]
            odd_product.append((l1[i],l1[j]))

print(odd_product)

     



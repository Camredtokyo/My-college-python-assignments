#A5_09. Write a program to calculate the mean of elements in a tuple of integers.

t= ()
n = int(input("Enter the no. of elements for the tuple: "))
print("Enter the elements: ")
for i in range (n):
    element = int(input(f'Enter element no. {i+1} : '))
    t+=(element,)
sum=0
count=0
for num in t:
    sum+=num
    count+=1

mean = sum/count    
    
    

print("Mean = ",mean)

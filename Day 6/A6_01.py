#A6_01.Write a program to create a dictionary that contains(i,i*i) such that i is an integer number between 1 and n
#(both included).

n = int(input("Enter the value of 'n' : "))
square_dict = {}
i = 1

while i <= n:
    square_dict[i] = i * i
    i = i + 1

print(square_dict)

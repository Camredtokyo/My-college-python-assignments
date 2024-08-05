#A3_02. Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter a number : "))
sum=0
stored_num=num

if num < 0:
    print("Armstrong number cannot be negative")
    pass

else:
    digits=len(str(num))
    
    while num != 0:
        num_digit = num % 10
        sum += num_digit ** digits
        num //= 10

    if sum == stored_num:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")

              

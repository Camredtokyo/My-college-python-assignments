# A3_03. Write a program to compute the LCM of two positive integers.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if num1<=0 or num2<=0:
    print("LCM is not defined for negative numbers")
    pass  
else:
    
    if num1>num2:
       max_num=num1
    else:
       max_num=num2
    
    lcm=max_num
 
    while True:
        
        if lcm%num1==0 and lcm%num2==0:
            print("LCM is : ",lcm)
            break  
        else:
            lcm+=max_num
            continue  

    

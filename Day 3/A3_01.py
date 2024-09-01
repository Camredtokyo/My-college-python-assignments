num=int(input("Enter a number : "))
if num <= 1:
    print("This is not a prime number.")
    pass  
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break  
        else:
            continue  
    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

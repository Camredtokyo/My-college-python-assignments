# A3_04. Write a program to find the sum of all prime numbers within a given range.

start=int(input("Enter the starting number : "))
end=int(input("Enter the ending number : "))

prime_sum = 0

for num in range(start, end + 1):
    is_prime = True
    if num < 2:
        continue
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_sum += num
    else:
        pass
print("Sum of prime numbers is",prime_sum)

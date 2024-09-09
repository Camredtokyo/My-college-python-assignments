# A6_02. Write a program to count the numbers of characters in a string and store them in a dictionary.

input_string = input("Enter a string : ")

char_count = {}
i = 0
while i < len(input_string):
    char = input_string[i]
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1
    i = i + 1

print(char_count)

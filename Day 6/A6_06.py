# Write a program to merge two dictionaries.

dict1 = {
    'a': 10,
    'b': 5,
    'c': 7
}
dict2 = {
    'd': 15,
    'e': 20,
    'f': 25
}
merged_dict = {}
for key in dict1:
    merged_dict[key]=dict1[key]
for key in dict2:
    merged_dict[key]=dict2[key]
    
print(merged_dict)

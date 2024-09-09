# Write a program to input player's name (string) and runs (integer) scored for n number of players where n should be 
# input from the keyboard. Store the player’s details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player otherwise return '-1' if the player's name is not found.

cricket = {}

n = int(input("Enter the number of players: "))

i = 0
while i < n:
    name = input(f"Enter the name of player {i + 1}: ")
    runs = int(input(f"Enter the runs scored by {name}: "))
    cricket[name] = runs
    i = i + 1

search_name = input("Enter the name of the player to search: ")

if search_name in cricket:
    print(f"Runs scored by {search_name}: {cricket[search_name]}")
else:
    print("-1")

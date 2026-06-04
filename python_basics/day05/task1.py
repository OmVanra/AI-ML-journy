# Q1
# . Create a program that:
# 1. Opens a file  
# "names.txt"
# in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

# Open the file in write mode and write names
with open("names.txt", 'w') as file:
    for i in range(5):
        name = input(f"Enter name {i + 1}:")
        file.write(name + "\n")

# Open the file in read mode and print names
with open("names.txt", 'r') as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())
        
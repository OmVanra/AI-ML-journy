# 2
# . Create a program that:
# 1. Opens a file  
# "log.txt"
# in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs

# Open the file in append mode and add a log entry
with open("log.txt", 'a') as file:
    log_entry = "Program run successfully"
    file.write(log_entry + "\n")

# Open the file in read mode and print all log entries
with open("log.txt" , 'r') as file:
    print("log entries in the file:")
    for line in file:
        print(line.strip())



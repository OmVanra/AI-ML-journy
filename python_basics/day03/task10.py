# # . Ask the user for a string and print:

# All unique characters
# • 
# The count of unique characters

def unique_characters():
    user_input = input("Enter a string: ")
    unique_chars = set(user_input)
    print(f"Unique characters: {unique_chars}")
    print(f"Count of unique characters: {len(unique_chars)}")

print("Welcome to the Unique Character Counter!")
unique_characters()

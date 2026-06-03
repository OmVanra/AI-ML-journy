# Given a list, print all elements that appear more than once in the list.
# [ 
# Hint- use sets]

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
# Example usage
input_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
duplicates = find_duplicates(input_list)
print(f"Duplicate elements in the list: {duplicates}")

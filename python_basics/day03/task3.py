# . Input two lists of integers from the user. Merge them into one list and sort the 
# result

def merge_and_sort_lists():
    list1 = input("Enter the first list of integers (comma separated): ")
    list2 = input("Enter the second list of integers (comma separated): ")
    
    # Convert the input strings to lists of integers
    list1 = [int(x) for x in list1.split(',')]
    list2 = [int(x) for x in list2.split(',')]
    
    # Merge the lists
    merged_list = list1 + list2
    
    # Sort the merged list
    merged_list.sort()
    
    return merged_list

# Example usage
result = merge_and_sort_lists()
print(f"The merged and sorted list is: {result}")
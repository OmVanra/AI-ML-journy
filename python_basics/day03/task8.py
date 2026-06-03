# . Write a program to check whether two lists share no common elements. 
#  share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]

def have_no_common_elements(list1, list2):
    return set(list1).isdisjoint(set(list2))

# Example usage
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
if have_no_common_elements(list1, list2):
    print("The lists share no common elements.")
else:
    print("The lists share common elements.")
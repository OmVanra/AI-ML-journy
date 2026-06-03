# Given a list of integers compute the average of all numbers in the list.

def compute_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
numbers = [10, 20, 30, 40, 50]
average = compute_average(numbers)
print(f"The average of the numbers is: {average}")


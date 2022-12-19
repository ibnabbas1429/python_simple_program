#
# 
# set the smallest and next smallest to infinity
def smallest(numbers):
    smallest_number = float('inf')
    next_smallest_number = float('inf')
    for num in numbers:
        if num <= smallest_number:
            smallest_number, next_smallest_number = num ,smallest_number
        elif num < next_smallest_number:
            next_smallest_number = num
    return f"smallest_number is {smallest_number} and next_smallest_number is {next_smallest_number}"

numbers = [111,20,53,24,15,67,9,23,11,84,56]

print(smallest(numbers))
# sum of the two lowest positive integers in an array

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sum(sorted_numbers[:2])
'''
Sum square difference
problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def sum_of_squares(range_number):
    sum_of_squares_list = []
    for i in range(1,range_number+1):
        sum_of_squares_list.append(int(i)**2)
    sum_of_squares = sum(sum_of_squares_list)
    return sum_of_squares
def square_of_sum(range_number):
    square_of_sum_list = [] 
    for i in range(1,range_number+1):
        square_of_sum_list.append(int(i))
    square_of_sum = (sum(square_of_sum_list))**2
    return square_of_sum
def sum_square_difference(range_number_for_both):
    sum_square_difference = square_of_sum(range_number_for_both) - sum_of_squares(range_number_for_both)
    return sum_square_difference

print(sum_square_difference(100))

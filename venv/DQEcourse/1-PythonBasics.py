#
import random
list_length = 100; probability_range = 1000 # define Length of the list and the Depth of probability
sorted_list = list(range(list_length)) # create dummy for sorted list
list_of_random_numbers = list(range(list_length)) # create dummy for random list
# create list with random number
for _ in range(list_length): list_of_random_numbers[_] = random.randint(1, probability_range)
# comprehension using: list_of_random_numbers_compr_using = [random.randint(1, probability_range) for i in range(list_length)]
print("------->: unsorted random List:")
print(list_of_random_numbers)
#sorting the List
for i in range(list_length):
    min_number = min(list_of_random_numbers)
    sorted_list[i] = min_number
    list_of_random_numbers.remove(min_number)
# an output for random and sorted lists
print("------->sorted random List:")
print(sorted_list)
# Sums calculation
even_sum = 0; odd_sum = 0
for i in range(list_length):
    if sorted_list[i] % 2 == 0: even_sum = even_sum + sorted_list[i]
for i in range(list_length):
    if sorted_list[i] % 2 == 1: odd_sum = odd_sum + sorted_list[i]
print("The sum of even numbers:", even_sum)
print("The sum of odd numbers:", odd_sum)

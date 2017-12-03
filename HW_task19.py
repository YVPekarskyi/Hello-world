import random

def find_max_of_n(num_limit, lower_bound, upper_bound):
    curr_max = lower_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound,upper_bound)
        print('rand. number:', rand_number)

        if rand_number > curr_max:
            curr_max = rand_number

    return curr_max

result1 = find_max_of_n(10, 20, 60)
print(result1)

def find_min_of_n(num_limit, lower_bound, upper_bound):
    curr_min = upper_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound,upper_bound)
        print('rand. number:', rand_number)

        if rand_number < curr_min:
            curr_min = rand_number

    return curr_min

result2 = find_min_of_n(5, 9, 30)
print(result2)

print ("Разница =", result1 - result2)
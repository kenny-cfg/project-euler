"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,  we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000

* loop through 1 - 1000
* filter in multiples of 3 and 5
* add them up
"""


# This is probably 'more Pythonic'
def solve_for(top_number):
    all_numbers = range(1, top_number)
    multiples_of_3_or_5 = filter(lambda x: x % 3 == 0 or x % 5 == 0, all_numbers)
    return sum(multiples_of_3_or_5)


def solve_for_second(top_number):
    sum = 0
    for x in range(1, top_number):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum


if __name__ == '__main__':
    answer = solve_for(1000)
    print(answer)

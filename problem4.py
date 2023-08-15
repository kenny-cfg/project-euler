"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

Approach:
* Work out all products of two 3-digit numbers
* Filter in the palindromes
* Return the maximum
"""
import math


def solution(digits):
    lowest_relevant_number = 10 ** (digits - 1)
    highest_relevant_number = 10 ** digits
    all_relevant_numbers = range(lowest_relevant_number , highest_relevant_number)
    all_relevant_products = [x * y for y in all_relevant_numbers for x in all_relevant_numbers]
    all_palindromes = filter(lambda x: str(x)[::-1] == str(x), all_relevant_products)
    return max(all_palindromes)


def solution_with_for_loops(digits):
    lowest_relevant_number = 10 ** (digits - 1)
    highest_relevant_number = 10 ** digits
    all_relevant_numbers = range(lowest_relevant_number , highest_relevant_number)
    candidate = 0
    for x in all_relevant_numbers:
        for y in all_relevant_numbers:
            product = x * y
            if str(product)[::-1] != str(product):
                continue
            if product > candidate:
                candidate = product
    return candidate


if __name__ == '__main__':
    answer = solution(3)
    answer_with_for_loops = solution_with_for_loops(3)
    print(answer)
    print(answer_with_for_loops)
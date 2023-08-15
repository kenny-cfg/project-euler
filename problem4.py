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
    # Work out range from 10 to 99
    all_relevant_numbers = range(10 ** (digits - 1), 10 ** digits)
    all_relevant_products = [x * y for y in all_relevant_numbers for x in all_relevant_numbers]
    all_palindromes = filter(lambda x: str(x)[::-1] == str(x), all_relevant_products)
    return max(all_palindromes)


if __name__ == '__main__':
    answer = solution(3)
    print(answer)
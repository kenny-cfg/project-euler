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
    for x in all_relevant_numbers:
        print(x)
    pass


if __name__ == '__main__':
    answer = solution(2)
    print(answer)
    print('Should be 9009')
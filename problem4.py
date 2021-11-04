"""
Date: 11/04/2021
Author: David Greybosh

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Fidn the largest palindrome made from the product of two 3-digit numbers.
"""

def check_palindrome(n: int):
    num_string = str(n)
    reverse_string = "".join(reversed(num_string))
    if num_string == reverse_string:
        return True
    return False

def make_palindromes():
    palindrome_list = []
    for i in range(100, 1001):
        for j in range(100, 1001):
            if check_palindrome(i * j):
                palindrome_list.append(i * j)
    return palindrome_list

def main():
    print(max(make_palindromes()))

if __name__ == '__main__':
    main()

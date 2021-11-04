"""
Date: 11/03/2021
Author: David Greybosh

If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 4, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    lst = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
    sum(lst)
    print(lst) 

if __name__ == '__main__':
    main()

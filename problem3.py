"""
Date: 11/04/2021
Author: David Greybosh

The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?
"""

def find_prime_factors(n: int):
    factor_list = []
    i = 2
    while n > 1:
        while n % i == 0:
            factor_list.append(i)
            n /= i
        i += 1
    return factor_list
            

def main():
    print(max(find_prime_factors(600851475143)))

if __name__ == '__main__':
    main()

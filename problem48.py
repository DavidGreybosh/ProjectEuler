"""
Date: 11/04/2021
Author: David Greybosh

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def main():
    total = 0
    for i in range(1, 1001):
        total += i ** i
    string = str(total)
    print("Last 10 Digits: " + string[-10:])
    
if __name__ == '__main__':
    main()

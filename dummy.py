# This is a dummy program to find prime numbers in a given interval

"""
Author: Dhanushki Mapitigama
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print("Prime numbers between 1 and 1000:")
    for num in range(1, 1001):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    main()


# This is a dummy program

def sieve_of_eratosthenes(limit): # ChatGPT gave this script - did not check the correctness
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for number in range(2, int(limit**0.5) + 1):
        if primes[number]:
            for multiple in range(number*number, limit + 1, number):
                primes[multiple] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]

def main():
    limit = 1000
    prime_numbers = sieve_of_eratosthenes(limit)
    print("Prime numbers between 1 and 1000:")
    print(prime_numbers)

if __name__ == "__main__":
    main()


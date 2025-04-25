# TTSSE-Lab1
Dummy repo for TTSSE Lab - on version control

This repo contains a python function to find prime numbers in a given interval.

Update:
Sieve of Eratosthenes method
Goal: Find all prime numbers up to a number n

-Create a list of numbers from 2 to n.
-Start with the first number in the list (which is 2). It is prime.
-Cross out all the multiples of 2 (e.g., 4, 6, 8, 10, etc.).
-Move to the next uncrossed number in the list. It is 3. Mark it as prime.
-Cross out all the multiples of 3.
-Repeat this process:
-Go to the next uncrossed number (e.g., 5, 7, etc.).
-Cross out all its multiples.
-Continue until you reach the square root of n.
-The remaining uncrossed numbers are all the prime numbers up to n.

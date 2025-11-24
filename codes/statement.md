1. Euler’s Totient Function – euler_phi(n)
You must write a function that calculates φ(n), the number of integers from 1 to n that are coprime with n (their gcd with n equals 1).


2. Möbius Function – mobius(n)
You must write a function to compute the Möbius µ(n) value:
1 → if n is square-free and has even number of distinct prime factors
−1 → if n is square-free and has odd number of distinct prime factors
0 → if n contains any repeated prime factor (a square)


3. Divisor Sum – divisor_sum(n)
You must write a function that returns the sum of all positive divisors of n (including 1 and n). This is the arithmetic divisor function σ(n).


4. Prime Counting Function – prime_pi(n)
You must write a function that counts how many prime numbers are ≤ n. This approximates the classical prime-counting function π(n), though you can use simple primality testing.


5. Legendre Symbol – legendre_symbol(a, p)
You must write a function that computes the Legendre symbol (a/p) for an odd prime p.
Using Euler’s criterion:
Compute a^((p–1)/2) mod p
If result is 1, a is a quadratic residue → return 1
If result is p−1, return −1
If a mod p = 0, return 0


6. factorial(n)
Write a function that returns n!, the product of all integers from 1 to n.


7. is_palindrome(n)
Write a function to check whether a number reads the same forwards and backwards.


8. mean_of_digits(n)
Write a function that returns the average of all digits in the number n.


9. digital_root(n)
Write a function that keeps summing digits until the number becomes a single digit.


10. is_abundant(n)
Write a function that returns True if the sum of proper divisors of n is greater than n.


11. is_deficient(n)
Write a function that returns True if the sum of proper divisors of n is less than n.


12. is_harshad(n)
Write a function to check if n is divisible by the sum of its digits.


13. is_automorphic(n)
Write a function that checks whether n² ends with n.


14. is_pronic(n)
Write a function that checks if n = k(k + 1) for some integer k.


15. prime_factors(n)
Write a function that returns the list of prime factors of n.


16. count_distinct_prime_factors(n)
Write a function that returns the number of unique prime factors of n.


17. is_prime_power(n)
Write a function to check if n = pᵏ for some prime p and k ≥ 1.


18. is_mersenne_prime(p)
Check whether 2ᵖ − 1 is prime (given p is prime).


19. twin_primes(limit)
Generate all twin prime pairs (p, p+2) up to the given limit.


20. count_divisors(n)
Write a function that counts how many positive divisors n has.


21. aliquot_sum(n)
Return the sum of proper divisors of n.


22. are_amicable(a, b)
Check whether a and b are amicable numbers:
σ(a) − a = b and σ(b) − b = a.


23. multiplicative_persistence(n)
Count how many steps you need until repeatedly multiplying digits gives a single digit.


24. is_highly_composite(n)
Check if n has more divisors than any number smaller than n.


25. mod_exp(base, exponent, modulus)
Compute (base^exponent) % modulus efficiently using fast exponentiation.


26. mod_inverse(a, m)
Find x such that:
(a * x) ≡ 1 (mod m).


27. crt(remainders, moduli)
Solve a system of linear congruences using the Chinese Remainder Theorem.


28. is_quadratic_residue(a, p)
Check if the congruence x² ≡ a (mod p) has a solution.


29. order_mod(a, n)
Find the smallest k such that:
aᵏ ≡ 1 (mod n).


30. is_fibonacci_prime(n)
Check if n is both a Fibonacci number and a prime.


31. lucas_sequence(n)
Generate the first n Lucas numbers (starting with 2, 1).


32. is_perfect_power(n)
Check if n = aᵇ for integers a > 1 and b > 1.


33. collatz_length(n)
Return the number of steps for n to reach 1 using the Collatz sequence.


34. polygonal_number(s, n)
Return the n-th s-gonal number.


35. is_carmichael(n)
Check whether composite n satisfies aⁿ⁻¹ ≡ 1 (mod n)
for all a coprime to n.


36. is_prime_miller_rabin(n, k)
Implement the Miller–Rabin probabilistic test with k rounds.


37. pollard_rho(n)
Implement Pollard’s rho algorithm for integer factorization.


38. zeta_approx(s, terms)
Approximate the Riemann zeta function ζ(s) using a series of given terms.


39. partition_function(n)
Compute p(n): the number of ways to write n as a sum of positive integers (order does not matter).

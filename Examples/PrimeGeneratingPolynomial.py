
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Polynomial import Polynomial
from random import randint
from typing import Tuple
from sympy.ntheory import isprime

# https://mathworld.wolfram.com/Prime-GeneratingPolynomial.html

limits = Tuple[int]

# Random PrimeGeneratingPolynomial Generator
def random_pgp(num: int = None, range: Tuple[int] = (1, 1000)) -> Tuple[Polynomial, limits]:
    if not num:
        p = randint(*range)
    else:
        p = num
    limits = Tuple[int]
    
    result_Poly = Polynomial([1, (1 - 2*p), (41 + p**2 - p)], var="n")

    i = 0
    while(isprime(result_Poly.value(x = i))):
        i+=1
    limits = (0, i - 1)
    if limits in [(0, 0), (0, -1)] :
        if num:
            return None, None
        result_Poly, limits = random_pgp()

    # (n - num)**2 + (n - num) + 41
    # = n**2 + (1 - 2*num)*n + 41 + num**2 - num 
    return result_Poly, limits

if __name__ == "__main__":
    prime_generator_poly, limits = random_pgp()
    print("Polynomial selected:", prime_generator_poly, "Limits:", limits)
    list_of_primes = []
    for i in range(*limits):
        list_of_primes.append(prime_generator_poly.value(x = i))
    print("Primes that can generated via this Polynomial", list_of_primes)
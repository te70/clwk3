from math import gcd
from functools import reduce

class EulerTotient:

    @staticmethod
    def basic_phi(n):
        # brute force method to compute phi(n)
        count = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                count += 1
        return count
    
    @staticmethod
    def prime_factors(n):
        #find unique prime factos of n
        i = 2
        factors = set()
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    @staticmethod
    def efficient_phi(n):
        #eulers product formula using prime factorization
        result = n
        for p in EulerTotient.prime_factors(n):
            result *= (1 - 1/p)
        return int(result)
    
    @staticmethod
    def verify_methods(n):
        basic = EulerTotient.basic_phi(n)
        efficient = EulerTotient.efficient_phi(n)
        assert basic == efficient, f"Mismatch as n={n}"
        return basic
    
if __name__ == "__main__":
    for n in range(2,21):
        phi = EulerTotient.verify_methods(n)
        print(f"phi({n}) = {phi}")


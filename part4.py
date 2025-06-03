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
    
    def sum_totients(n):
        total = sum(EulerTotient.efficient_phi(d) for d in range(1, n+1) if n % d == 0)
        return total
    
if __name__ == "__main__":
    for n in range(1,21):
        s = EulerTotient.sum_totients(n)
        print(f"sum of all phi(d) for all d | {n} = {s} {'g'if s==n else 'n'}")
        assert s == n
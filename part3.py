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
        #find unique prime factors of n
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
    
    #section 2 part 2
if __name__ == "__main__":
    a, b = 5, 8
    phi_ab = EulerTotient.efficient_phi(a * b)
    phi_a = EulerTotient.efficient_phi(a)
    phi_b = EulerTotient.efficient_phi(b)

    print(f"phi({a}x{b}) = phi({a})xphi({b}) -> {phi_ab} = {phi_a}x{phi_b}")
    assert phi_ab == phi_a * phi_b

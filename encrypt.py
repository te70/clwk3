import random
from math import gcd

class PrimeGenerator:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def generate_primes(start, end):
        return [x for x in range(start, end) if PrimeGenerator.is_prime(x)]

class KeyGenerator:
    def __init__(self, start=10, end=100):
        self.primes = PrimeGenerator.generate_primes(start, end)
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None

    def select_primes(self):
        self.p = random.choice(self.primes)
        self.q = random.choice(self.primes)
        while self.q == self.p:
            self.q = random.choice(self.primes)
    
    def compute_keys(self):
        self.select_primes()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        self.e = random.choice([x for x in range(2, self.phi) if gcd(x, self.phi) == 1])
        self.d = self.mod_inverse(self.e, self.phi)

    def mod_inverse(self, e, phi):
        t, new_t = 0, 1
        r, new_r = phi, e
        while new_r != 0:
            quotient = r // new_r
            t, new_t = new_t, t - quotient * new_t
            r, new_r = new_r, r - quotient * new_r
        if t < 0:
            t += phi
        return t
    
    def get_keys(self):
        return {
            "p": self.p,
            "q": self.q, 
            "n": self.n,
            "phi": self.phi,
            "e (public exponent)": self.e,
            "d (private exponent)": self.d
        }
    
if __name__ == "__main__":
    keygen = KeyGenerator(start=50, end=100)
    keygen.compute_keys()
    keys = keygen.get_keys()

    print("Generated key components")
    for k, v in keys.items():
        print(f"{k}: {v}")

    #correctness check
    assert (keys['d (private exponent)'] * keys['e (public exponent)']) % keys['phi'] == 1
    print("\n Key generation verified using Euler's Totient function")
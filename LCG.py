
class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        # Initialize the LCG with a seed, multiplier, increment, and modulus.
        self.state = seed  # The current state is initialized with the seed value.
        self.a = a         # Multiplier (a well-known default value).
        self.c = c         # Increment (a default common value).
        self.m = m         # Modulus (often set to 2^32 for 32-bit RNGs).

    def next(self):
        # Calculate the next value in the sequence using the LCG formula.
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def generate_sequence(self, count=10):
        # Generate a sequence of random numbers.
        return [self.next() for _ in range(count)]  # Store and return sequence in list

# Example Usage
''' lcg = LCG(seed=1234)  # Create an LCG instance with a seed of 1234
sequence = lcg.generate_sequence(10)  # Generate 10 random numbers
print(sequence)  # Print the sequence '''


class MersenneTwister:
    def __init__(self, seed):
        # Initialize the Mersenne Twister with a seed
        self.index = 624
        self.mt = [0] * 624  # Create an array to store the state
        self.mt[0] = seed  # Set the initial state as the seed
        
        for i in range(1, 624):
            self.mt[i] = (0x6c078965 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i) & 0xffffffff
    
    def twist(self):
        for i in range(624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] ^= 0x9908b0df
        self.index = 0
    
    def next(self):
        if self.index >= 624:
            self.twist()  # If all numbers are used, "twist" to generate new numbers
        
        y = self.mt[self.index]
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)
        
        self.index += 1
        return y & 0xffffffff  # Return the next random number
    
    def generate_sequence(self, count=10):
        # Generate a sequence of random numbers
        return [self.next() for _ in range(count)]

# Example Usage
'''mt = MersenneTwister(seed=1234)  # Create a Mersenne Twister instance with a seed of 1234
sequence = mt.generate_sequence(10)  # Generate 10 random numbers
print(sequence)'''

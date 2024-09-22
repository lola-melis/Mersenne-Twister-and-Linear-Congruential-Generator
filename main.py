import time
from LCG import LCG
from MersenneTwister import MersenneTwister
from save_sequence import save_sequence_to_binary_file

# Generate and save LCG sequence in binary format
lcg_seed = int(time.time())
lcg = LCG(seed=lcg_seed)
lcg_sequence = lcg.generate_sequence(25000000)  # Generate 1000 random numbers
save_sequence_to_binary_file(lcg_sequence, "lcg_sequence.bin")

# Generate and save Mersenne Twister sequence in binary format
mt_seed = int(time.time())
mt = MersenneTwister(seed=mt_seed)
mt_sequence = mt.generate_sequence(25000000)  # Generate 1000 random numbers
save_sequence_to_binary_file(mt_sequence, "mt_sequence.bin")


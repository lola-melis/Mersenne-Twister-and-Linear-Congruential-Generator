# Pseudo Random Number Generators

This project contains implementations of two well-known random number generators (RNGs) used in various applications, including slot machines: the Linear Congruential Generator (LCG) and the Mersenne Twister (MT). The project also includes functionality for generating random number sequences and saving them in binary format for further testing.

## Project Structure

- **LCG.py**: This file contains the implementation of a Linear Congruential Generator (LCG). The LCG generates a sequence of pseudo-random numbers based on the formula:
X_{n+1} = (aX_n + c) % m
where `a`, `c`, and `m` are constants, and `X` is the current state (seed). The file allows for generating a sequence of random numbers.

- **MersenneTwister.py**: This file contains the implementation of the Mersenne Twister algorithm, a widely used PRNG known for its high quality and long period. The file provides functionality to generate a sequence of random numbers using the MT19937 algorithm.

- **save_sequence.py**: This file includes a utility function to save a generated sequence of random numbers into a binary file. Each number is written as 4 bytes, making the file suitable for testing with statistical randomness tools like DieHarder.

- **main.py**: This is the main entry point of the project. It:
1. Generates a random number sequence using the LCG with a time-based seed.
2. Generates a random number sequence using the Mersenne Twister with a time-based seed.
3. Saves both sequences to binary files (`lcg_sequence.bin` and `mt_sequence.bin`), which can be used for further analysis and testing.

## Usage

1. **LCG Random Numbers**:
 - Create an instance of the `LCG` class with a seed and generate random sequences.
 - Example usage:
   ```python
   lcg = LCG(seed=1234)
   sequence = lcg.generate_sequence(10)
   print(sequence)
   ```

2. **Mersenne Twister Random Numbers**:
 - Create an instance of the `MersenneTwister` class with a seed and generate random sequences.
 - Example usage:
   ```python
   mt = MersenneTwister(seed=1234)
   sequence = mt.generate_sequence(10)
   print(sequence)
   ```

3. **Save Sequence**:
 - Use the `save_sequence_to_binary_file` function to save generated sequences into a binary file.
 - Example usage:
   ```python
   save_sequence_to_binary_file(sequence, "filename.bin")
   ```

## DieHard Test Suite

The **DieHard Test Suite** is a collection of tests designed to evaluate the quality of random number generators by subjecting the generated sequences to rigorous statistical analysis. In this project, the generated sequences from both the LCG and Mersenne Twister algorithms are saved in binary format and tested using the DieHarder suite.

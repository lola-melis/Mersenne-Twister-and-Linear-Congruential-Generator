def save_sequence_to_binary_file(sequence, filename):
    with open(filename, "wb") as f:
        for number in sequence:
            f.write(number.to_bytes(4, byteorder="little"))

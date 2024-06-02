
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]


PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def hex_to_bin(hex_string):
    """
    Convert a hex string to a binary string.
    """
    return bin(int(hex_string, 16))[2:].zfill(64)

def bin_to_hex(bin_string):
    """
    Convert a binary string to a hex string.
    """
    return hex(int(bin_string, 2))[2:].upper().zfill(16)

def permute(block, table):
    """
    Permute the input block using the specified table.
    """
    return ''.join([block[table[i] - 1] for i in range(len(table))])

def shift_left(block, n):
    """
    Left shift the block by n bits.
    """
    return block[n:] + block[:n]

def generate_subkeys(key):
    """
    Generate 16 subkeys from the original 64-bit key.
    """

    permuted_key = permute(key, PC1)
    

    left_half = permuted_key[:28]
    right_half = permuted_key[28:]

    subkeys = []
    for round_number in range(16):

        left_half = shift_left(left_half, SHIFT_SCHEDULE[round_number])
        right_half = shift_left(right_half, SHIFT_SCHEDULE[round_number])
        

        combined_key = left_half + right_half
        subkey = permute(combined_key, PC2)
        subkeys.append(subkey)
    
    return subkeys

def main():

    hex_key = input("Enter a 16-character hexadecimal key (0-9, A-F): ").strip()
    print(f"Original Key (hex): {hex_key}")

    bin_key = hex_to_bin(hex_key)
    print(f"Original Key (binary): {bin_key}")
    
    subkeys = generate_subkeys(bin_key)

    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1} (binary): {subkey}")
        print(f"Subkey {i+1} (hex): {bin_to_hex(subkey)}")

if __name__ == "__main__":
    main()

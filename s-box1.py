# S-box 1 Table
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def hex_to_bin(hex_string):
    """
    Convert a hex string to a binary string.
    """
    return bin(int(hex_string, 16))[2:].zfill(6)

def bin_to_hex(bin_string):
    """
    Convert a binary string to a hex string.
    """
    return hex(int(bin_string, 2))[2:].upper().zfill(1)

def s_box_substitution(input_bits, s_box):
    """
    Perform substitution using the specified S-box.
    """
    # The input bits are 6 bits long
    row = int(input_bits[0] + input_bits[5], 2)  # First and last bits
    col = int(input_bits[1:5], 2)                # Middle four bits
    return bin(s_box[row][col])[2:].zfill(4)     # Convert to 4-bit binary

def main():
    # Example 6-bit block (in hexadecimal)
    hex_input = input("Enter a 1-character hexadecimal value (0-F): ").strip()
    print(f"Input (hex): {hex_input}")

    # Convert hex input to binary
    bin_input = hex_to_bin(hex_input)
    print(f"Input (binary): {bin_input}")

    # Apply S-box 1 substitution
    s_box_output = s_box_substitution(bin_input, S1)
    print(f"After S-box 1 Substitution (binary): {s_box_output}")
    print(f"After S-box 1 Substitution (hex): {bin_to_hex(s_box_output)}")

if __name__ == "__main__":
    main()


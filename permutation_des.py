
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]


FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(data, table):
    """
    Perform permutation on the given data using the specified table.
    """
    permuted_data = [data[i - 1] for i in table]
    return permuted_data

def hex_to_binary(hex_string):
    """
    Convert hexadecimal string to binary string.
    """
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def binary_to_hex(binary_string):
    """
    Convert binary string to hexadecimal string.
    """
    return hex(int(binary_string, 2))[2:].zfill(len(binary_string) // 4)


hex_input = input("Enter a 16-character hexadecimal input: ")


binary_input = hex_to_binary(hex_input)


ip_result = permute(list(map(int, binary_input)), IP)
ip_binary = ''.join(map(str, ip_result))


fp_result = permute(ip_result, FP)
fp_binary = ''.join(map(str, fp_result))


ip_hex = binary_to_hex(ip_binary)
fp_hex = binary_to_hex(fp_binary)

print("Initial permutation (IP) - Binary:", ip_binary)
print("Initial permutation (IP) - Hexadecimal:", ip_hex)
print("Final permutation (FP) - Binary:", fp_binary)
print("Final permutation (FP) - Hexadecimal:", fp_hex)

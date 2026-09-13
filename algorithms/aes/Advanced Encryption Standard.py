import os
import time
"""S-Box substitution table for AES"""
S_BOX = [
    #  0     1    2    3    4    5    6    7    8    9    A    B    C    D    E    F
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

"""S-Box substitution table for AES Inverse"""
INV_S_BOX = [
    #  0     1    2    3    4    5    6    7    8    9    A    B    C    D    E    F
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
]

"""Round Constant for Key Expansion"""
Rcon = [
    0x00,  # AES starts from index 1, so index 0 is unused.
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D
]

"""Applies S-Box substitution to each byte in the state matrix"""
def sub_bytes(state, s_box):
    for i in range(4):  # Iterate over rows
        for j in range(4):  # Iterate over columns
            state[i][j] = s_box[state[i][j] >> 4][state[i][j] & 0x0F]  # S-box lookup
    return state

"""Shifts rows of the state matrix left by increasing offsets"""
def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]  # Shift row 1 left by 1
    state[2] = state[2][2:] + state[2][:2]  # Shift row 2 left by 2
    state[3] = state[3][3:] + state[3][:3]  # Shift row 3 left by 3
    return state

"""Inverse ShiftRows: Shifts rows of the state matrix right by increasing offsets."""
def inv_shift_rows(state):
    state[1] = state[1][-1:] + state[1][:-1]  # Shift row 1 right by 1
    state[2] = state[2][-2:] + state[2][:-2]  # Shift row 2 right by 2
    state[3] = state[3][-3:] + state[3][:-3]  # Shift row 3 right by 3
    return state

"""Galois Field multiplication of a and b in GF(2^8)"""
def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:               # If the least significant bit of b is set, XOR p with a
            p ^= a
        hi_bit_set = a & 0x80   # Check if high bit (8th bit) is set
        a <<= 1                 # Multiply by x (shift left)
        if hi_bit_set:          # If the high bit was set before shift, reduce modulo AES polynomial
            a ^= 0x1B           # AES reduction polynomial x^8 + x^4 + x^3 + x + 1
        b >>= 1                 # Move to the next bit in b
    return p & 0xFF             # Ensure result is a byte

"""Applies MixColumns transformation to the state matrix"""
def mix_columns(state):
    for col in range(4):  # Process each column
        a = state[0][col]
        b = state[1][col]
        c = state[2][col]
        d = state[3][col]

        state[0][col] = gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1)
        state[1][col] = gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1)
        state[2][col] = gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3)
        state[3][col] = gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2)
    return state

"""Applies Inverse MixColumns transformation to the state matrix."""
def inv_mix_columns(state):
    for col in range(4):  # Process each column
        a = state[0][col]
        b = state[1][col]
        c = state[2][col]
        d = state[3][col]

        state[0][col] = gmul(a, 0x0E) ^ gmul(b, 0x0B) ^ gmul(c, 0x0D) ^ gmul(d, 0x09)
        state[1][col] = gmul(a, 0x09) ^ gmul(b, 0x0E) ^ gmul(c, 0x0B) ^ gmul(d, 0x0D)
        state[2][col] = gmul(a, 0x0D) ^ gmul(b, 0x09) ^ gmul(c, 0x0E) ^ gmul(d, 0x0B)
        state[3][col] = gmul(a, 0x0B) ^ gmul(b, 0x0D) ^ gmul(c, 0x09) ^ gmul(d, 0x0E)
    return state

"""XORs the state with the round key"""
def add_round_key(state, round_key):
    for i in range(4):  # 4 rows
        for j in range(4):  # 4 columns
            state[i][j] ^= round_key[i][j]  # XOR operation
    return state

"""Rotates a 4-byte word left by one byte"""
def rot_word(word):
    return word[1:] + word[:1]

"""Applies S-Box substitution to each byte of a word"""
def sub_word(word, s_box):
    return [s_box[b >> 4][b & 0x0F] for b in word]

"""Generates round keys from the initial AES key"""
def key_expansion(key, num_rounds):
    key_size = len(key)

    if key_size == 16:
        num_words = 44   # AES-128: 10 rounds
        expected_rounds = 10
    elif key_size == 24:
        num_words = 52   # AES-192: 12 rounds
        expected_rounds = 12
    elif key_size == 32:
        num_words = 60   # AES-256: 14 rounds
        expected_rounds = 14
    elif key_size == 64:
        num_words = 92   # Custom AES-512: 22 rounds
        expected_rounds = 22
    elif key_size == 128:
        num_words = 156  # Custom AES-1024: 38 rounds
        expected_rounds = 38
    else:
        raise ValueError(
            "Invalid key size. Must be 16, 24, 32, 64, or 128 bytes."
        )

    if num_rounds != expected_rounds:
        raise ValueError(
            f"AES-{key_size * 8} requires {expected_rounds} rounds."
        )

    # Generate initial key schedule (first N words are the original key)
    key_schedule = [list(key[i:i+4]) for i in range(0, key_size, 4)]

    for i in range(key_size // 4, num_words):
        temp = key_schedule[i - 1].copy()

        if i % (key_size // 4) == 0:
            temp = sub_word(rot_word(temp), S_BOX)
            rcon_index = i // (key_size // 4)
            temp[0] ^= Rcon[rcon_index]

        # Generalize the AES-256 rule to the two custom extensions.
        elif key_size >= 32 and i % (key_size // 4) == 4:
            temp = sub_word(temp, S_BOX)

        new_word = [
            key_schedule[i - (key_size // 4)][j] ^ temp[j]
            for j in range(4)
        ]
        key_schedule.append(new_word)

    # Convert key schedule into 4x4 round keys
    round_keys = []
    for i in range(0, num_words, 4):
        round_key = [[key_schedule[i + col][row] for col in range(4)] for row in range(4)]
        round_keys.append(round_key)

    return round_keys

"""Encrypts 16-byte block using AES encryption"""
def aes_encrypt(plaintext, key, num_rounds):
    round_keys = key_expansion(key, num_rounds)
    state = [[plaintext[4 * col + row] for col in range(4)] for row in range(4)]

    # Initial round key addition
    state = add_round_key(state, round_keys[0])

    # Main rounds (num_rounds - 1 rounds)
    for round in range(1, num_rounds):
        state = sub_bytes(state, S_BOX)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round])

    # Final round (without MixColumns)
    state = sub_bytes(state, S_BOX)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[num_rounds])

    ciphertext = [
        state[row][col]for col in range(4) for row in range(4)]
    return bytes(ciphertext)

"""Decrypts 16-byte block using AES decryption"""
def aes_decrypt(ciphertext, key, num_rounds):
    round_keys = key_expansion(key, num_rounds)
    state = [[ciphertext[4 * col + row] for col in range(4)] for row in range(4)]

    # Initial AddRoundKey with the last round key
    state = add_round_key(state, round_keys[num_rounds])

    for round in range(num_rounds - 1, 0, -1):
        state = inv_shift_rows(state)
        state = sub_bytes(state, INV_S_BOX)

        state = add_round_key(state, round_keys[round])

        if round > 0:
            state = inv_mix_columns(state)
    # Final round (no InvMixColumns)
    state = inv_shift_rows(state)

    state = sub_bytes(state, INV_S_BOX)

    state = add_round_key(state, round_keys[0])

    plaintext = [
        state[row][col] for col in range(4) for row in range(4)]
    return bytes(plaintext)

"""Converts ASCII text to a list of hexadecimal values"""
def ascii_to_hex_list(text):
    if len(text) != 16:
        raise ValueError("Input must be exactly 16 ASCII characters.")
    return [ord(c) for c in text]

"""Converts a list of hexadecimal values to ASCII text"""
def hex_list_to_ascii(hex_list):
    if len(hex_list) != 16:
        raise ValueError("Input must be exactly 16 integers.")
    ascii_text = ''.join([chr(byte) if 32 <= byte <= 126 else '.' for byte in hex_list])
    return ascii_text

# Key sizes: 16, 24, 32, 64, or 128 bytes
# Variants: 128, 192, 256, 512, or 1024 bits
key_size = 128 # Use 128 for the 1024-bit extension

#for i in range(100000):
key = list(os.urandom(key_size))
#key_hex = "000102030405060708090a0b0c0d0e0f"  # 32 hex chars = 16 bytes
# Manual conversion
#key = bytes([int(key_hex[i:i+2], 16) for i in range(0, len(key_hex), 2)])

print(f"\nKey (AES-{key_size * 8}):", [hex(byte) for byte in key])

# Text to be encrypted (must be exactly 16 characters)
#text = "00112233445566778899aabbccddeeff"  # 16-character input (note the trailing space)
text = "HELLOOOOOOOOOOOO"  # 16-character input (note the trailing space)
hexatext = ascii_to_hex_list(text)
#hexatext = bytes([int(text[i:i+2], 16) for i in range(0, len(text), 2)])

num_rounds = {16: 10, 24: 12, 32: 14, 64: 22, 128: 38}[key_size]

start = time.perf_counter()

ciphertext = aes_encrypt(hexatext, key, num_rounds)
end = time.perf_counter()
#elapsed_ns = (end - start)
#print(f"Execution time: {elapsed_ns} ns")
#print(f"Execution time: {elapsed_ns / 1e6:.3f} ms")

#print("Plaintext:", text)
print("Hexa text:", [hex(byte) for byte in hexatext])
print("Cipher text:", [hex(byte) for byte in ciphertext])

uncipherhtext = aes_decrypt(ciphertext, key, num_rounds)
#print("UnCipher hexa text:", [hex(byte) for byte in uncipherhtext])

unciphertext = hex_list_to_ascii(uncipherhtext)
print("UnCipher text:", unciphertext)
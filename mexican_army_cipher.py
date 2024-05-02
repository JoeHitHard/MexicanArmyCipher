import random

class MexicanArmyCipher:
    def __init__(self, ring_offsets, encode_to_text=False):
        self.ring_offsets = ring_offsets
        self.alphabets = "abcdefghijklmnopqrstuvwzyz"
        self.rotated_texts = self.rotate_list(ring_offsets[0])
        self.encode_to_text = encode_to_text

    def rotate_list(self, ring_offset):
        lst = list(self.alphabets)
        ring_offset = ring_offset % len(self.alphabets)
        return ''.join(lst[-ring_offset:] + lst[:-ring_offset])

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                encrypted_text += random.choice(self.ring_offsets)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                pass
            else:
                decrypted_text += char
        return decrypted_text

    def shift_char(self, char, offset):
        if char.islower():
            base = ord('a')
        elif char.isupper():
            base = ord('A')
        else:
            return char

        shifted = (ord(char) - base + offset) % 26 + base
        return chr(shifted)


# Example usage:
cipher = MexicanArmyCipher([10, 28, 74, 95], False)

plaintext = "Network Security"
encrypted_text = cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)

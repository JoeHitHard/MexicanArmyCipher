import random


class MexicanArmyCipher:
    def __init__(self, start_letter, ring_offsets, encode_to_text=False):
        self.start_letter = start_letter.lower()
        self.ring_offsets = ring_offsets
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.rotated_alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.rings = self.rotate_list(ring_offsets)
        self.encode_to_text = encode_to_text

    def rotate_list(self, rings_offset):
        start_ind = self.alphabets.index(self.start_letter)
        rotated_chars_list = list(self.alphabets)
        self.rotated_alphabets = ''.join(rotated_chars_list[start_ind:] + rotated_chars_list[:start_ind])
        rings = []
        for i in range(4):
            ring = [j + (26 * i) for j in range(1, 26 + 1)]
            if len(rings_offset) > i:
                ring_offset = rings_offset[i] - 1
                ring_offset = ring_offset % len(self.alphabets)
                ring = ring[ring_offset:] + ring[:ring_offset]
            rings.append(ring)
        return rings

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                encoded_char = random.choice(self.rings)[self.rotated_alphabets.index(char.lower())]
                if encoded_char > 100 :
                    encoded_char = random.choice(self.rings[:-1])[self.rotated_alphabets.index(char.lower())]
                if self.encode_to_text :
                    encoded_char = self.alphabets[encoded_char - 1 % 26]
                else:
                    encoded_char = str(encoded_char) + '-'
                encrypted_text += encoded_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        cipher_list = list(ciphertext.split('-'))
        for char in cipher_list:
            if char.isnumeric():
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
cipher = MexicanArmyCipher('m', [10, 28, 74, 95], False)

plaintext = "Network Security"
encrypted_text = cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)

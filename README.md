
# 🔐 Mexican Army Cipher: A Python Cryptographic Adventure

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to the **Mexican Army Cipher** – a unique cryptographic tool inspired by historical cipher techniques, reimagined for modern Python enthusiasts. Whether you're a cryptography hobbyist, a developer exploring secure encoding, or a recruiter seeking creative coders, this project offers a fascinating blend of history, math, and programming. Let's dive in!

---

## 🚀 Features

- **Dynamic Alphabet Rotation**: Start with any letter to shuffle the cipher's base alphabet.
- **Multi-Ring Encryption**: Encode messages across 4 configurable rings with custom offsets.
- **Dual Output Modes**: Choose between numeric codes or hybrid text/number representations.
- **Randomized Encoding**: Each character maps to multiple possible values for enhanced security.
- **Simple API**: Straightforward `encrypt()` and `decrypt()` methods for easy integration.

---

## 🛠️ Technologies Used

- **Python 3.8+** (Core implementation)
- **Random Module** (For cryptographic operations)
- **Git** (Version control)
- **PyCharm IDE** (Development environment)

---

## ⚡ Quick Start

### Installation
```bash
git clone https://github.com/JoeHitHard/MexicanArmyCipher.git
cd MexicanArmyCipher

### Basic Usage
```python
from mexican_army_cipher import MexicanArmyCipher

# Initialize cipher with custom parameters
cipher = MexicanArmyCipher(
    start_letter='M',          # Base alphabet rotation point
    ring_offsets=[10,28,74,95],# Ring configuration
    encode_to_text=False       # Output format toggle
)

# Encrypt a message
plaintext = "Secret Message"
encrypted = cipher.encrypt(plaintext)  # Returns "11-2-17-20-76-15-..."

# Decrypt back to original
decrypted = cipher.decrypt(encrypted)  # Returns "secret message"
```

---

## 🌟 Sample Use Cases

1. **Secure Team Communication**  
   Encode sensitive project codenames during development sprints.

2. **Educational Tool**  
   Teach cryptography concepts with hands-on examples.

3. **API Key Obfuscation**  
   Add an extra layer of protection for sensitive strings.

4. **Capture-the-Flag Challenges**  
   Create engaging cybersecurity puzzles.

---

## 🔄 Dual Encoding Modes

### Numerical Mode (Default)
```python
# encode_to_text=False
cipher = MexicanArmyCipher('M', [10,28,74,95], False)
print(cipher.encrypt("Hello"))  # Output: "42-8-33-33-60"
```

### Hybrid Text Mode
```python
# encode_to_text=True
cipher = MexicanArmyCipher('M', [10,28,74,95], True)
print(cipher.encrypt("Hello"))  # Output: "1q-0h-1h-1h-2d"
```

---

## 🧠 How It Works (Briefly)

1. **Alphabet Rotation**  
   The cipher starts by rotating the standard alphabet based on your chosen letter (e.g., 'M' → "mnopqrstuvwxyzabcdefghijkl").

2. **Ring Configuration**  
   Four encryption rings are created with offsets that determine their rotational positions.

3. **Randomized Mapping**  
   Each plaintext character maps to multiple possible cipher values from different rings, chosen randomly during encryption.
---

_Developed with ❤️ by Joseph Hit Hard_  
_"In cryptography we trust, but we still verify!"_

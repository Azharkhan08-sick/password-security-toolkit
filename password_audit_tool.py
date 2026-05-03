# Password Security Analysis Toolkit (Simulated)
# Author: Your Name

import hashlib
import string
import math

def generate_dictionary(base_words):
    mutations = []
    for word in base_words:
        mutations.append(word)
        mutations.append(word + "123")
        mutations.append(word + "2024")
        mutations.append(word.capitalize())
        mutations.append(word.replace("a", "@").replace("e", "3"))
    return list(set(mutations))

def hash_passwords(password_list):
    hashed = {}
    for pwd in password_list:
        hash_val = hashlib.sha256(pwd.encode()).hexdigest()
        hashed[pwd] = hash_val
    return hashed

def brute_force_estimate(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    total_combinations = len(chars) ** length
    attempts_per_sec = 1_000_000
    seconds = total_combinations / attempts_per_sec
    return total_combinations, seconds

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(not c.isalnum() for c in password): pool += 32
    return len(password) * math.log2(pool) if pool else 0

def check_strength(password):
    entropy = calculate_entropy(password)
    if entropy < 30:
        strength = "Weak"
    elif entropy < 60:
        strength = "Medium"
    else:
        strength = "Strong"
    return strength, round(entropy, 2)

def main():
    print("=== PASSWORD SECURITY ANALYSIS TOOL ===\n")
    base_words = ["admin", "user", "password", "india", "mumbai"]

    dictionary = generate_dictionary(base_words)
    print(f"[+] Generated {len(dictionary)} passwords\n")

    hashed = hash_passwords(dictionary)
    print("[+] Sample Hashes:")
    for i, (pwd, h) in enumerate(hashed.items()):
        if i == 5:
            break
        print(f"{pwd} -> {h}")
    print()

    print("[+] Password Strength Analysis:\n")
    for pwd in list(dictionary)[:10]:
        strength, entropy = check_strength(pwd)
        print(f"{pwd:15} | {strength:6} | Entropy: {entropy}")

    print()

    print("[+] Brute Force Simulation:")
    length = 6
    combos, seconds = brute_force_estimate(length)

    print(f"Password Length: {length}")
    print(f"Total combinations: {combos}")
    print(f"Estimated time: {round(seconds, 2)} seconds (~{round(seconds/3600, 2)} hours)")

if __name__ == "__main__":
    main()

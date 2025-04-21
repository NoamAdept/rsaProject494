#!/usr/bin/env python3
"""
Noam Yakar CSE 494 RSA Implementation
RSA Implementation: generate private key, encrypt, decrypt using big primes expressed as (2^e - c).
"""
import argparse


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Return a tuple (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return (a, 1, 0)
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (gcd, x, y)


def generate_private_key(e: int, p: int, q: int) -> int:
    """
    Compute d = e^{-1} mod phi(n), where phi(n) = (p-1)*(q-1).
    """
    phi = (p - 1) * (q - 1)
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e and phi(n) are not coprime, gcd={}".format(gcd))
    return x % phi


def decrypt(ciphertext: int, d: int, N: int) -> int:
    """
    Decrypt ciphertext C with private key d and modulus N.
    """
    return pow(ciphertext, d, N)


def encrypt(plaintext: int, e: int, N: int) -> int:
    """
    Encrypt plaintext M with public key e and modulus N.
    """
    return pow(plaintext, e, N)


def parse_big_number(exp: int, minus_c: int) -> int:
    """
    Compute 2^exp - minus_c to reconstruct the large integer.
    """
    return pow(2, exp) - minus_c


def main():
    parser = argparse.ArgumentParser(description="RSA encryption/decryption tool")
    parser.add_argument("--p_e", type=int, required=True, help="Exponent for p (compute p = 2^p_e - p_c)")
    parser.add_argument("--p_c", type=int, required=True, help="Subtraction constant for p")
    parser.add_argument("--q_e", type=int, required=True, help="Exponent for q (compute q = 2^q_e - q_c)")
    parser.add_argument("--q_c", type=int, required=True, help="Subtraction constant for q")
    parser.add_argument("--e_e", type=int, required=True, help="Exponent for e (compute e = 2^e_e - e_c)")
    parser.add_argument("--e_c", type=int, required=True, help="Subtraction constant for e")
    parser.add_argument("--ciphertext", type=int, required=True, help="Ciphertext to decrypt")
    parser.add_argument("--plaintext", type=int, required=True, help="Plaintext to encrypt")
    args = parser.parse_args()

    # Reconstruct large primes and exponent values
    p = parse_big_number(args.p_e, args.p_c)
    q = parse_big_number(args.q_e, args.q_c)
    e = parse_big_number(args.e_e, args.e_c)
    N = p * q

    # Generate private key d
    d = generate_private_key(e, p, q)

    # Perform decryption and encryption
    decrypted = decrypt(args.ciphertext, d, N)
    encrypted = encrypt(args.plaintext, e, N)

    # Output as comma-separated: decrypted_text,encrypted_ciphertext
    print(f"{decrypted},{encrypted}")


if __name__ == "__main__":
    main()

# RSA Project

This repository contains a Python implementation of the RSA algorithm, including key generation, encryption, and decryption using very large prime numbers expressed as \(2^e - c\).

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Keys & Running](#generating-keys--running)
  - [Arguments](#arguments)
  - [Example](#example)
- [How It Works](#how-it-works)
  - [Reconstructing Big Numbers](#reconstructing-big-numbers)
  - [Extended Euclidean Algorithm](#extended-euclidean-algorithm)
  - [Encryption & Decryption](#encryption--decryption)
- [License](#license)

---

## Prerequisites

- Python 3.7 or higher
- No external libraries required—only built-in Python modules are used.

---

## Files

- `rsa.py` — Main script implementing:
  - `generate_private_key(e, p, q)`
  - `encrypt(plaintext, e, N)`
  - `decrypt(ciphertext, d, N)`
  - `extended_gcd(a, b)` helper for modular inverse
  - `parse_big_number(exp, minus_c)` to rebuild big integers
- `README.md` — This file

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://your.repo.url/rsa-project.git
   cd rsa-project
   ```

2. Ensure you’re using Python 3.x:
   ```bash
   python3 --version
   ```

---

## Usage

### Generating Keys & Running

All parameters are passed via command-line flags to `rsa.py`.

```bash
python3 rsa.py \
  --p_e <p_exponent> --p_c <p_constant> \
  --q_e <q_exponent> --q_c <q_constant> \
  --e_e <e_exponent> --e_c <e_constant> \
  --ciphertext <ciphertext_int> \
  --plaintext <plaintext_int>
```

The script will:
1. Reconstruct primes \(p, q\) and exponent \(e\).
2. Compute modulus \(N = p \times q\).
3. Compute private key \(d\) using the Extended Euclidean algorithm.
4. Decrypt the provided ciphertext.
5. Encrypt the provided plaintext.
6. Output `decrypted,encrypted` as a comma-separated pair.

### Arguments

- `--p_e` — Exponent for prime \(p\) (compute \(p = 2^{p_e} - p_c\)).
- `--p_c` — Subtraction constant for \(p\).
- `--q_e` — Exponent for prime \(q\) (compute \(q = 2^{q_e} - q_c\)).
- `--q_c` — Subtraction constant for \(q\).
- `--e_e` — Exponent for public exponent \(e\) (compute \(e = 2^{e_e} - e_c\)).
- `--e_c` — Subtraction constant for \(e\).
- `--ciphertext` — Integer ciphertext to decrypt.
- `--plaintext` — Integer plaintext to encrypt.

### Example

Using the sample from the assignment description:

```bash
python3 rsa.py \
  --p_e 252 \
  --p_c 3551320294972622704085158542068617432155596220113794691428435278300674188689 \
  --q_e 261 \
  --q_c 1194103838696593800434465377182188669000022374589724805392034067440035954998819 \
  --e_e 26 \
  --e_c 12320055 \
  --ciphertext 2109636589475319481690033161025118722547237230723991210476034408842255762453948587714804726263356891979001833011601694803200495628743260668599194164851838 \
  --plaintext 6024799506
```

Expected output:
```
6024799506,2109636589475319481690033161025118722547237230723991210476034408842255762453948587714804726263356891979001833011601694803200495628743260668599194164851838
```

---

## How It Works

### Reconstructing Big Numbers

Given a pair \((e, c)\), the true value is computed as:

\[
  x = 2^e - c
\]

This allows handling primes and exponents far beyond normal ranges.

### Extended Euclidean Algorithm

To find the private key \(d\), we solve:

\[
  e \times d \equiv 1 \pmod{\varphi(n)}
\]

where

\[
  \varphi(n) = (p-1)(q-1).
\]

Our `extended_gcd(a, b)` returns \((\gcd, x, y)\) such that:

\[
  a x + b y = \gcd(a,b).
\]

From that we extract the modular inverse of \(e\).

### Encryption & Decryption

- **Encrypt:** \(C = M^e \bmod N\)
- **Decrypt:** \(M = C^d \bmod N\)

---

## License

This project is released under the [MIT License](LICENSE).


Author: Érick Oliveira
Date: 06/29/18

RSA Algorithm Implementation with Python

Functions:

1 - Generate private and puclic keys
2 - Encrypt with decimal output
3 - Decrypt with decimal input

How it works?

n = p*q
phi(n) = (p-1)*(q-1)
1 < e < phi(n), e and phi(n) are coprimes
d*e is congruent to 1 mod phi(n) a.k.a multiplicative inverse of e in phi(n)

Encrypt: m^e is congruent to c mod n, m is every message letter
Decrypt: c^d is congruent to m mod n, c is every encoded letter

*The original algorithm is a property of RSA Security
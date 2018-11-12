# RSA Algorithm Implementation with Python

Author: Érick Oliveira
Date: 11/10/2018

## Functions:

- Generate private and puclic keys
- Encrypt
- Decrypt

## How it works?

- n = p*q
- phi(n) = (p-1)*(q-1)
- 1 < e < phi(n), e and phi(n) are coprimes
- d*e is congruent to 1 mod phi(n) a.k.a multiplicative inverse of e in phi(n)

- **Encrypt:** m^e is congruent to c mod n, m is every message letter
- **Decrypt:** c^d is congruent to m mod n, c is every encoded letter

*The original algorithm is a property of RSA Security Inc.
 
### Usage
```sh
$ python rsa.py
```
Then, follow the interative menu

### Explaining 'Low Processing Mode'

It's a way to reduce the process and consequently increase the speed with which the keys are calculated.
Instead of calculating all valid possibilities for 'e' and then randomizing and using one of them, the algorithm will soon use the first valid value of 'e' found.

### For Linux or Mac Users

 - You will have to eliminate all calls for lambda functions declared on lines 7 and 8. It does not cause any efect to the algorithm, it's just for the visual.
 - You can replace the 'cls' on clear function to 'clear' if you want. You all can print a bunch of '\n' to simulate a page cleaner.
 
 **The original algorithm is a property of RSA Security Inc.**
from random import randint
import sys
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

def is_prime(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

def calc_e(totn):
  x = True
  while x == True:
    div_e = []
    div_totn = []
    e = randint(2,totn-1)   
    for i in range(2,totn+1):
      if totn%i == 0:
        div_totn.append(i)
    for i in range(2,e+1):
      if e%i == 0:
        div_e.append(i)   
    if len(div_e) > len(div_totn):
      bigger = div_e
      smaller = div_totn
    else:
      bigger = div_totn
      smaller = div_e
    x = False
    for i in range(0,len(bigger)):
      for j in range(0,len(smaller)):
        if smaller[j] == bigger[i]:
          x = True 
  return e

def inv_mult(e, totn):
	for d in range(2,totn):
		de = d*e
		if de%totn == 1:
			return d

def generate_keys():
	print("\t Generate Keys\n")
	x = False
	while x == False:
		p = int(input('Insert a prime number p: '))
		x = is_prime(p)
		if x == False:
			print(str(p) + ' is not a prime number')
	x = False
	while x == False:
		q = int(input('Insert a prime number q: '))
		x = is_prime(q)
		if x == False:
			print(str(q) + ' is not a prime number')
	n = p*q
	totn = (p-1)*(q-1)
	e = calc_e(totn)
	d = inv_mult(e,totn)
	print("\nPublic Keys:")
	print("n = " + str(n))
	print("e = " + str(e))
	print("\nPrivate Keys:")
	print("p = " + str(p))
	print("q = " + str(q))
	print("d = " + str(d) + '\n')
	pause()
	clear()
	menu()
	
def encode(message, n, e):
	print("Encrypted message:\n")
	for i in message:
		m = ord(i)
		me = m ** e #m^e
		c = me%n
		print(c, end=' ')
	print("\n\n")
	pause()
	clear()
	menu()

def decode(message, p, q, d):
  message += ' '
  n = p*q
  buff = ''
  ant = 0
  atual = 0
  print("Decrypted message:\n")
  for atual in range(0,len(message)):
    if message[atual] == ' ':
      for i in range(ant,atual):
        buff += message[i]
      c = int(buff)
      cd = c ** d #c^d
      m = cd%n
      print(chr(m), end="")
      buff = ''
      ant = atual+1
  print('\n\n')
  pause()
  clear()		
  menu()

def menu():
	print('\t RSA Algorithm\n')
	print(' 1 - Generate keys\n 2 - Encode\n 3 - Decode\n 4 - Exit\n')
	op = int(input('Option: '))
	if op == 1:
		clear()
		generate_keys()
	elif op == 2:
		clear()
		print("Enter the public keys\n")
		n = int(input("n = "))
		e = int(input("e = "))
		clear()
		message = input("Enter your message:\n\n")
		clear()
		encode(message, n, e)
		encode()
	elif op == 3:
		clear()
		print("Enter the private keys\n")
		p = int(input("p = "))
		q = int(input("q = "))
		d = int(input("d = "))
		clear()
		message = input("Enter the encrypted message:\n\n")
		clear()
		decode(message, p, q, d)
		decode()
	elif op == 4:
		sys.exit()

menu()
from multiprocessing import Process
from random import choice
import time
import sys
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = ' '
pos = '¨¨'
pos += lower + upper + numbers + special

def is_prime(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True

def verify_divisors(vt1, vt2):
  for i in vt1:
    for j in vt2:
      if i == j and i != 1:
        return True
  return False

def get_e_lowProcessing(totn):
  tn_divisors = []
  for i in range(1,totn+1):
    if totn % i == 0:
      tn_divisors.append(i)
  pos_e = []
  e = 2
  while e < totn:
    e_divisors = []
    for i in range(1,e+1):
      if e % i == 0:
        e_divisors.append(i)
    flag = verify_divisors(tn_divisors, e_divisors)
    if flag == False:
        return e
    else:
      e += 1

def get_e(totn):
  tn_divisors = []
  total = (2*totn)-2
  cont = 0
  for i in range(1,totn+1):
    cont += 1
    p = (100*cont)/total
    p = round(p,2)
    print('Calculing Public Keys: ', end='')
    print(str(p) + ' %')
    clear()
    if totn % i == 0:
      tn_divisors.append(i)
  pos_e = []
  e = 2
  while e < totn:
    e_divisors = []
    cont += 1
    p = (100*cont)/total
    p = round(p,2)
    print('Calculing Public Keys: ', end='')
    print(str(p) + ' %')
    clear()
    for i in range(1,e+1):
      if e % i == 0:
        e_divisors.append(i)
    flag = verify_divisors(tn_divisors, e_divisors)
    if flag == False:
      pos_e.append(e)
    e += 1
  e = choice(pos_e)
  return e

def inv_mult(e, totn):
	for d in range(2,totn):
		de = d*e
		if de%totn == 1:
			return d

def encode(msg, n, e):
  global buff
  buff = ''
  print('\nEncrypted message:\n')
  for i in msg:
    m = pos.find(i)
    me = m ** e
    c = me % n
    print(str(c), end=' ')
    buff += str(c) + ' '
  print('\n')

def decode(msg, p, q, d):
  msg += ' '
  n = p*q
  buff = ''
  ant = 0
  atual = 0
  print('\nDecrypted message:\n')
  for atual in range(0,len(msg)):
    if msg[atual] == ' ':
      for i in range(ant,atual):
        buff += msg[i]
      c = int(buff)
      cd = c ** d #c^d
      m = cd%n
      print(pos[m], end='')
      buff = ''
      ant = atual+1
  print('\n')

def generate_keys():
  print('\tGenerate Keys\n')
  p = int(input('p = '))
  if (is_prime(p) == False or p < 11):
    print('\nInvalid input!\n')
    print('p must be a prime number bigger than 11\n')
    pause()
    clear()
    generate_keys()
  q = int(input('q = '))
  if (is_prime(q) == False or p < 11):
    print('\nInvalid input!\n')
    print('q must be a prime number bigger than 11\n')
    pause()
    clear()
    generate_keys()
    sys.exit()
  op = input('\nEnable Low Processing Mode (Faster but less secure)? (y/n) ')
  if op == 'y' or op == 'Y':
    reduce_processing = True
    clear()
  else:
    reduce_processing = False
  start = time.time()
  n = p*q
  totn = (p-1)*(q-1)
  if reduce_processing:
    e = get_e_lowProcessing(totn)
  else:
    e = get_e(totn)
  d = inv_mult(e, totn)
  end = time.time()
  tempo = int(end - start)
  hr = int(tempo/3600)
  tempo = tempo%3600
  mn = int(tempo/60)
  tempo = tempo%60
  sec = tempo

  print('Public keys:\n')
  print('n = ' + str(n))
  print('e = ' + str(e) + '\n')
  print('Private keys:\n')
  print('p = ' + str(p))
  print('q = ' + str(q))
  print('d = ' + str(d) + '\n')

  print('Time elapsed: ' + str(hr) + 'h ' + str(mn) + 'min ' + str(sec) + 's\n')
  
  op = input('Save to file? (y/n) ')
  if op == 'Y' or op == 'y':
    arq = open('keys.txt', 'w')
    arq.write('Public keys:\n')
    arq.write('n = ' + str(n) + '\n')
    arq.write('e = ' + str(e) + '\n')
    arq.write('Private keys:\n')
    arq.write('p = ' + str(p) + '\n')
    arq.write('q = ' + str(q) + '\n')
    arq.write('d = ' + str(d) + '\n')
    arq.close()
  #os.system('keys.txt')
  print('\n\n')
  pause()

def menu():
  print('\tChoose an Option\n')
  print('1 - Generate keys')
  print('2 - Encode')
  print('3 - Decode')
  print('4 - Exit\n')
  op = int(input('Option: '))
  if op == 1:
    clear()
    generate_keys()
    clear()
    menu()
  elif op == 2:
    clear()
    print('\tEncode\n')
    n = int(input('n = '))
    e = int(input('e = '))
    msg = input('\nMessage:\n\n')
    encode(msg, n, e)
    print('\n')
    pause()
    clear()
    menu()
  elif op == 3:
    clear()
    print('\tDecode\n')
    p = int(input('p = '))
    q = int(input('q = '))
    d = int(input('d = '))
    msg = input('\nMessage:\n\n')
    decode(msg, p, q, d)
    print('\n')
    pause()
    clear()
    menu()
  elif op == 4:
    sys.exit()

os.system('color 0a')
menu()
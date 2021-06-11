import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '()[]{},;:.-/\\?+*#!@$%^&<>_ '

#This can be adjusted according to what you want your password to be
#Lets's say you dont want any symbols, just change syms to be False etc
upper, lower, nums, syms = True, True, True, True

all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols
  
#Adjustable
length = 20
amount = 20
count = 0

for x in range(amount):
    count = count + 1
    password = ''.join(random.sample(all, length))
    print("Password", count, ":", password)
#Included count to keep track of number of password generated

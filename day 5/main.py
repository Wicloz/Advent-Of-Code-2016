import hashlib
import random

input = 'wtnhxymk'
password = '________'

index = 0
while '_' in password:
    hash = hashlib.md5((input + str(index)).encode('utf-8')).hexdigest()
    good_hash = True
    for i in range(0, 5):
        if hash[i] is not '0':
            good_hash = False
            break
    if good_hash and hash[5].isdigit() and int(hash[5]) in range(0, 8) and password[int(hash[5])] is '_':
        password = password[:int(hash[5])] + hash[6] + password[int(hash[5])+1:]
        print(password)
    index += 1

print(index)

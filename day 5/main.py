import hashlib

input = 'wtnhxymk'
password = ''

index = 0
while len(password) < 8:
    print(index)
    hash = hashlib.md5((input + str(index)).encode('utf-8')).hexdigest()
    good_hash = True
    for i in range(0, 5):
        if hash[i] is not '0':
            good_hash = False
            break
    if good_hash:
        password += hash[5]
    index += 1

print(password)

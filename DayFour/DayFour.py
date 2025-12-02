import hashlib

with open('input.txt', 'r') as input:
    secret_key = input.read().strip()

n = 1

while True:
    candidate = secret_key +str(n)
    digest = hashlib.md5(candidate.encode()).hexdigest()

    #Part One is 5 0's, Part Two is 6 0's
    if digest.startswith('000000'):
        print(n)
        break

    n += 1
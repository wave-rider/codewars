import time
sextuplets = []

start = time.time()
def is_prime(i):
    if   i<=1: return False
    elif i==2: return True
    else:
        for j in range(3, int(i**0.5), 2):
            if i%j==0:  return False
        return True

def all_6tuplets():
    for i in range(3*10**5):
        p = 30*i + 7
        if is_prime(p) and is_prime(p+4) and is_prime(p+6) and is_prime(p+10) and is_prime(p+12) and is_prime(p+16):
            sextuplets.append([p, p+4, p+6, p+10, p+12, p+16])

all_6tuplets()

def find_primes_sextuplet(sum_limit):
    for tuplet in sextuplets:
        if sum(tuplet)>=sum_limit:  return tuplet


r = find_primes_sextuplet(29700000)
end = time.time()
print(end-start)
print(r)

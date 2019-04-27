import time

start = time.time()
def find_primes_sextuplet(sum_limit):
    p = (sum_limit - 48) // 6 + 1
    if not p%2:
        if p%3 == 2: p += 3
        else: p += 1
    elif p%2 and p%3 == 0: p += 2

    while 1:
        lst = [p+x for x in (0,4,6,10,12,16)]
        for i in xrange(3, 1+int(lst[-1]**0.5), 2):
            if not all(num%i for num in lst): break
        else: return lst
        if p%3 == 2: p += 2
        else: p += 4

r = find_primes_sextuplet(29700000)
end = time.time()
print(end-start)
print(r)

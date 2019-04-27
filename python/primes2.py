import numpy, time

memoPrimes, primesL, memoDict = set(), [], {}
def primesfrom2to(n):
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def build_primes_data(limit):
    global memoPrimes, primesL
    primesL = primesfrom2to(limit).tolist()
    memoPrimes = set(primesL)


def find_primes_sextuplet(sum_limit):
    global memoPrimes, primesL, memoDict
    steps = [0, 4, 6, 10, 12, 16]
    if memoDict == {}:
        build_primes_data(50000000)
        for p in  primesL:
            pS = []
            for s in steps:
                if p + s not in memoPrimes: break
                pS.append(p + s)
            if len(pS) == 6:
                memoDict[sum(pS)] = tuple(pS)
    for sum_ in sorted(memoDict.keys()):
        if sum_ > sum_limit:
            return list(memoDict[sum_])

start = time.time()
r = find_primes_sextuplet(29700000)
end = time.time()
print(end-start)
print(r)

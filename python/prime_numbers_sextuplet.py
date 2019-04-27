'''
We are interested in collecting the sets of six prime numbers,
that having a starting prime p, the following values are also primes
forming the sextuplet ```[p, p + 4, p + 6, p + 10, p + 12, p + 16]```

The first sextuplet that we find is ```[7, 11, 13, 17, 19, 23]```

The second one is ```[97, 101, 103, 107, 109, 113]```

Given a number ```sum_limit```, you should give the first sextuplet
which sum (of its six primes) surpasses the sum_limit value.
'''
import time

start = time.time()
sextuplets = []

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


prime_list = primes(6005904)

def find_sextuplets():
    my_queue = [0] * 6
    the_rule = [0, 4, 6, 10, 12, 16]
    index = 0

    while sum(my_queue) < 29700000:
        rule_index = 1
        k = index
        while rule_index < 6 and prime_list[index] + the_rule[rule_index] == prime_list[k+1]:
            rule_index += 1
            k+=1

        if rule_index == 6:
            my_queue = prime_list[index:index + 6]
            sextuplets.append(my_queue)
        index += 1

    return my_queue

find_sextuplets()

def find_primes_sextuplet(sum_limit):
    for tuplet in sextuplets:
        if sum(tuplet)>=sum_limit:
            return tuplet

r = find_primes_sextuplet(29700000)
end = time.time()
print(end-start)
print(r)

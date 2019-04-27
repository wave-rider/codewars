'''
We are interested in collecting the sets of six prime numbers,
that having a starting prime p, the following values are also primes
forming the sextuplet ```[p, p + 4, p + 6, p + 10, p + 12, p + 16]```

The first sextuplet that we find is ```[7, 11, 13, 17, 19, 23]```

The second one is ```[97, 101, 103, 107, 109, 113]```

Given a number ```sum_limit```, you should give the first sextuplet
which sum (of its six primes) surpasses the sum_limit value.
'''
def find_primes_sextuplet(sum_limit):
    my_queue = [0] * 6
    the_rule = [0, 4, 6, 10, 12, 16]
    rule_sum = sum(the_rule)
    init = (sum_limit - 1 - rule_sum)// 6
    current_number = 2
    prime_list = [2]
    current_prime_index = 0
    while sum(my_queue) < sum_limit:
        current_number += 1
        max_prime = (current_number) // 2
        index = 0
        prime_found = True

        while prime_list[index] <= max_prime:
            if current_number % prime_list[index] == 0:
                prime_found = False
                break
            index += 1

        if prime_found:
            prime_list.append(current_number)
            current_prime_index += 1
            if current_number >= init and current_prime_index > 6:
                j = current_prime_index
                rule_index = 5
                while j > current_prime_index - 5 and prime_list[current_prime_index - 5] + the_rule[rule_index] == prime_list[j]:
                    j -= 1
                    rule_index -= 1
                if rule_index == 0:
                    my_queue =  prime_list[current_prime_index - 5:]
            print(init, current_number, current_prime_index)
    return my_queue

r = find_primes_sextuplet(2000)
print(r)

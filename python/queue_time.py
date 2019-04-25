def queue_time(customers, n):
    if len(customers) is 0:
        return 0
    index = n
    tills = customers[0:n]
    total = 0
    while index < len(customers):
        minimum_time = min(tills)
        till_index = 0
        total += minimum_time
        while till_index < n:
            tills[till_index] -= minimum_time
            if index < len(customers) and tills[till_index] == 0 :
                tills[till_index] = customers[index]
                index += 1
            till_index += 1
    return total + max(tills)

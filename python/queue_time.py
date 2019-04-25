def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

#a = queue_time([5,3,4], 1)
#print(a)

a = queue_time([2,3,10], 2)
print(a)


a = [1,2,3,67,89]
for index, item in enumerate(a):
    print(index, item)

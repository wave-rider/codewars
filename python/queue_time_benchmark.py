from random import seed
from random import randint
import time
import heapq

seed(1)
customers = []
n = 1000
for _ in range(100000):
	value = randint(0, 10)
	customers.append(value)

def show_time(function, customers, n):
    start = time.time()
    function(customers, n)
    end = time.time()
    print(str(function), ":", end-start)

def queue_time_siebenschlaefer(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

def queue_time_rovando(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

def queue_time_sort(customers, n):
    queues = [0] * n
    for i in customers:
        queues.sort()
        queues[0] += i
    return max(queues)

def queue_time_pan(customers, n):
  fcus=customers[:n]
  for c in range(n,len(customers)):
    fcus[fcus.index(min(fcus))] += customers[c]
  if len(fcus)== 0:
    return 0
  else:
    return max(fcus)

show_time(queue_time_siebenschlaefer, customers, n)
show_time(queue_time_rovando, customers, n)
show_time(queue_time_pan, customers, n)
show_time(queue_time_sort, customers, n)


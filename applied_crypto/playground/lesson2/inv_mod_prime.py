import time

a1 = 14
p1 = 101

a2 = 102721840089015263978980446
p2 = 6768924473842051155435121

a3 = 78
a4 = 87618764987168109238743892512
start = time.perf_counter()
print(pow(a1, p1 - 2, p1))
t1 = time.perf_counter()
print(t1 - start)
print(pow(a2, p2 - 2, p2))
t2 = time.perf_counter()
print(t2 - t1)
print(pow(a3, p2 - 2, p2))
t3 = time.perf_counter()
print(t3 - t2)
print(pow(a4, p2 - 2, p2))
stop = time.perf_counter()
print(stop - t3)


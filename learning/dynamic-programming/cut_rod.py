import random
import time

from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

size = int(input("length of rod? "))

prices = [random.randint(0, size ** 2) for i in range(size)]
print(prices)

def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q

init_time = time.time()
max_profit = cut_rod(prices, size)
end_time = time.time()

print(f"max profit: {max_profit}, time: {end_time - init_time} (recursive)")


@lru_cache
def cached_cut_rod(n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(n):
        q = max(q, prices[i], cached_cut_rod(n - i - 1))
    return q

init_time = time.time()
max_profit = cached_cut_rod(size)
end_time = time.time()

print(f"max profit: {max_profit}, time: {end_time - init_time} (cached / dynamic)")


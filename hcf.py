def hcf(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    for i in range(1 + min(a, b) // 2, 0, -1):
        if a % i == b % i == 0:
            return i


first = 23
second = 69

print('HCF of', first, 'and', second, 'is', hcf(first, second))
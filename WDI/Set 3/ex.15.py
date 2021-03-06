# 15. We have a given array. Write program checking whether each number which index is one of the Fibonacci sequence
# elements is composite and, apart from this, if there is also at least one prime number in that array. To determine
# if number is prime I use sieve of Eratosthenes. 


def sieve(aux_arr, n):
    p = 2
    while p * p <= n:
        for x in range(2*p, n, p):
            aux_arr[x] = 0
        p += 1
    return arr


def ex15(arr):
    n = max(arr) + 1
    aux_arr = [1]*n
    sieve(aux_arr, n)
    a, b = 1, 1
    while b < len(arr):
        if aux_arr[arr[b]]:
            return False
        a, b = b, a+b
    for x in range(len(arr)):
        if aux_arr[arr[x]]:
            return True
    return False


arr = [20, 4, 6, 8, 5, 34, 56]
print(ex15(arr))
# Program will return true, because everything is ok, but if we change, for instance, 5 to 50 then it'll be false,
# because it won't be any prime number.

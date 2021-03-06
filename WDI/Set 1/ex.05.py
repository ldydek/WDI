# 5. Write program computing square root of a given number using Newton's formula.
# Solution: We can think about it in this way: at first we have a rectangle 1xn, where "n" is
# our given number. Our goal is to change length of rectangle sides to obtain a square, but
# its surface has to be the same all the time.
# "a", "b" - dimensions and "e" - as square root can be irrational we let an acceptable difference between "a" and "b"
# when we can break the loop.


def ex5(n):
    a, b = 1, n
    while abs(b-a) > 10**(-5):
        a = (a+b)/2
        b = n/a
    return a


print(ex5(25))

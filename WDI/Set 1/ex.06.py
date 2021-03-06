# 6. Write program solving equation x^x = 2020 by bisection method.
# Solution: at first we initialize variables for 4 and for 5, because 4^4 = 256 is smaller and 5^5 = 3125 is bigger
# than 2020. Later if ((0+5)/2)**((0+5)/2) is bigger than 2020 or not we change variable "a" or "b" and repeat the
# same until we achieve given accuracy or find a solution.

def ex6():
    a, b = 4, 5
    while b-a > 10**(-4):
        x = (a+b)/2
        if x**x == 2020:
            return x
        elif x**x > 2020:
            b = x
        else:
            a = x
    return (a+b)/2


print(ex6())


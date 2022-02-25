# Problem 1 ------------------------------------------------------------

def count_even(L):

    amount = 0

    for i in L:
        if i % 2 == 0:
            amount += 1

    return amount


L = [1,2,3,4,5,6,7,8]

print(count_even(L))


# Problem 2 ------------------------------------------------------------

def list_to_str(lis):
    result = ''
    for i in lis:
        result += str(i) + ' '

    return result

print(list_to_str([1,2,3]))


# Problem 3 ------------------------------------------------------------

def list_are_the_same(list1, list2):
    same = True

    for x in range(0, len(list2)):
        if list1[x] != list2[x]:
                same = False

    return same


print(list_are_the_same([1,2,3,4],[1,2,3,4,5]))


# 1, 2, 3
# 1, 2, 3

# Problem 4 ------------------------------------------------------------

def simplify_fraction(n,m):
    max = 0
    gcd = 0

    if n > m:
        max = n

    else:
        max = m

    for i in range(1, max):
        if n % i == 0 and m % i == 0:
            gcb = i


    return n//gcb , m//gcb

print(simplify_fraction(3,6))

# Probelm 5 ------------------------------------------------------------
import math

def leibniz_formula(n):
    total = 0

    for i in range(0,n+1):
        total += 4*(((-1)**i)/(2*i+1))

    return total

def round_down(value, decimals):
    factor = 1 / (10 ** decimals)
    return (value // factor) * factor


def close_to_pi(n):

    common = 0

    for i in range(0,n):
        if round_down(leibniz_formula(n), i) == round_down(math.pi, i):
            common += 1

        else:
            break

    print("Approximation is" , common ,"digits similar to pi")


close_to_pi(100)


# Problem 6 ------------------------------------------------------------

def euclid(n,m):

    check = True

    while check:
        if m < n:
            (m,n) = (n,m)

        if (m % n) == 0:
            check = False
            return n

        else:
            n = m % n


print(euclid(30,12))




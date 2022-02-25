# Lab 10

# Problem 1
def power(x,n):
    count = 0
    if n == 0:
        return 1

    else:
        return x * power(x, n-1)

# Problem 2
def interleave(L1, L2):
    if len(L1) == 0:
        return L1 + L2

    else:
        return [L1[0] , L2[0]] + interleave(L1[1:], L2[1:])

# Problem 3
def reverse(L):
    if len(L) <= 1:
        return L
    else:
        return reverse(L[1:]) + [L[0]]

# Problem 4
def zigzag(L):
    n = len(L)
    mid = n//2

    if len(L) == 0:
        return

    if len(L) == 1:
        print(L[0], end = ' ')

    else:
        print(L[mid], L[mid-1], end = ' ')
        L.remove(L[mid])
        L.remove(L[mid-1])
        zigzag(L)




# Problem 5
def is_balanced(s):
    bracket1 = s.count("(")
    bracket2 = s.count(")")

    if bracket1 == bracket2:
        return True
    else:
        return False

# .find for strings -- try this

# Problem 6
print("goodbye and thank you")

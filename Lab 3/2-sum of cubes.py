#Sums of Cubes

def get_cube(n):
    '''Computes values in consecutive cubes
    n = value of last number cubed '''

    for i in range(1, n+1):
        print(i ** 3)


def cube_sum(n):
    ''' Computes sum of consecutive cubes using formula
    n = value of last number cubed '''

    sum = ((n**2)*(n+1)**2)/4
    return sum

def check_sum(n):
    ''' Checks sum of consecutive cubes using loop and formula, then
        compares them
    n = value of last number cubed'''

    global total

    for i in range(1, n+1):
        total += (i ** 3)

    if total == cube_sum(n):
        return True
    else:
        return False


def check_sums_up_to_n(N):
    '''Checks if the forumla for sum of consecutive cubes works for
        all number greater than n
    N = a value greater than n '''

    global total
    total = 0
    n = 1
    works = 0

    while n <= N:
        for i in range(1, n+1):
            total += (i ** 3)

        if total == cube_sum(n):
            works = True
            n += 1
            total = 0

        else:
            return False

    return works




if __name__ == '__main__':
    total = 0
    get_cube(4)
    print(cube_sum(4))
    print(check_sum(6))
    print(check_sums_up_to_n(5))
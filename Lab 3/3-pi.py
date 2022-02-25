#π

def leibniz_formula(n):
    ''' Use Leibniz Formula to find a close approximation for pi
    n = number inputed into the formula
    '''

    global total

    for i in range(0,n+1):
        total += 4*(((-1)**i)/(2*i+1))

    return total


if __name__ == "__main__":
    total = 0
    print(leibniz_formula(100)) #returns a value close to pi
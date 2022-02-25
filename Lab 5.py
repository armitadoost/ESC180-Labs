# Lab 5 - Lists and Loops

#Problem 1 --------------------------------------------------------------------

def list1_starts_with_list2(list1, list2):

    equal = False

    if len(list1) <= len(list2):
        for i in range (0,len(list1)):
            if list1[i] == list2[i]:
                equal = True
            else:
                return False

    return equal


print(list1_starts_with_list2([1,2,3],[1,3,3,4]))


# Problem 2 --------------------------------------------------------------------

def match_pattern(list1, list2):

    pattern = False

    for i in range (0,len(list1)):
        if list2 == list1[i:i+len(list2)]:
            pattern = True

    return pattern

list1 = [4, 10, 2, 3, 50, 100]
list2 = [2, 3, 50]
print(match_pattern(list1, list2))

# Problem 3 --------------------------------------------------------------------

def repeats(list0):

    for i in range(0, len(list0)):
        if list0[i] == list0[i+1] or list0[i] == list0[i-1]:
            return True

        else:
            return False


print(repeats([1,1,3,2,4,3]))


#Problem 4 --------------------------------------------------------------------

def print_matrix_dim(M):
    row = len(M[1])
    column = len(M)

    print(column , "x" , row)

print_matrix_dim([[1,2],[3,4],[5,6] ])

def mult_M_v(M, v):

    column_m = len(M)
    row_m = len(M[1])
    column_v = len(v)
    cell = []

    if row_m == column_v:
        for i in range(0, column_m):
            for x in range(0,column_v,2):
                adding_in = M[i][x] * v[x] + M[i][x+1] * v[x+1]
                cell.append(adding_in)


    return cell

print(mult_M_v([[2,3],[4,5],[6,7]], [2,3]))


def mult_M_v(M,v):
    res = []
    for row in M:
        sum = 0
        for i in range(len(v)):
            sum += row[i]+v[i]

        res.append(sum)

    return res

print(mult_M_v([[2,3],[4,5],[6,7]], [2,3]))

#Challenge --------------------------------------------------------------------

def matrix_mult(M, N):
     row_M = len(M[1])
     column_M = len(M)

     row_N = len(N[1])
     column_N = len(N)

     answer = []

     if row_M == column_N:
         answer *= row_M
        # row_M x column_N

        for i in range(0,len(M)):

            for x in range(0,len(N)):
                answer.append()


M = [[2, 4, 8],
     [1, 3, 6]]

N = [[1, 9],
     [4, 2],
     [3, 7]]

print(matrix_mult(M, N))


# Lab 7 - Guassian Elimination

#Needed for array() and dot()
from numpy import *

#Problem 1 --------------------------------------------------------------------
def print_matrix(M_lol):
    '''Return nested list M_lol as matrix'''
    M = array(M_lol)
    M_listoflists = M.tolist()
    return M_listoflists

# Problem 2 --------------------------------------------------------------------
def get_lead_ind(row):
    '''Return the index of the first non-zero element of row.
       Return len(row) if no non-zero elements'''
    zeros = 0

    for i in range(0,len(row)):
        if row[i] == 0:
            zeros += 1

        elif row[i] != 0:
            return i

    if zeros == len(row):
        return len(row)

# Problem 3 --------------------------------------------------------------------
def get_row_to_swap(M, start_i):
    M = print_matrix(M)
    min = 0

    lead_given = get_lead_ind(M[start_i])

    for i in range(start_i, len(M)):
        lead = get_lead_ind(M[i])

        if lead < lead_given and lead != get_lead_ind(M[min]):
            min = i
    if min == 0:
        return M

    else:
        M[start_i], M[min] = M[min], M[start_i]
        return M


# Problem 4 --------------------------------------------------------------------
def add_rows_coefs(r1, c1, r2, c2):
    ''' Return a new list for c1*r1 and c2*r2
        r1 and r2 are lists
        c1 and c2 are floats '''

    new_r1 = [0] * len(r1)

    for mult in range(len(r1)):
        new_r1[mult] = (c1*r1[mult]) + (c2*r2[mult])


    return new_r1

# Problem 5 --------------------------------------------------------------------
def eliminate(M, row_to_sub, best_lead_ind):

    given_lead = M[row_to_sub][get_lead_ind(M[row_to_sub])]

    for i in range(row_to_sub+1, len(M)):
        lead_value = M[i][best_lead_ind]

        if lead_value != 0:
            coef = (-1 * lead_value) / given_lead

            M[i] = add_rows_coefs(M[row_to_sub], coef, M[i], 1)

    return M

# Problem 6 --------------------------------------------------------------------
def forward_step(M):
    for sub in range(len(M)):
        M = get_row_to_swap(M, sub)
        print("Now looking at row" , sub)
        print("The matrix is currently:\n" , M)

        M = eliminate(M, sub, sub)
        print("Adding row" , sub, "to the rows below it")
        print("The matrix is currently:\n" , M)
        print(" ")

    return M

    # Help with the last 2 rows !!!!!

# Problem 7 --------------------------------------------------------------------
def back_eliminate(M, row, col):

    for i in range(row-1, -1, -1):

        if M[i][col] != 0:
            coef = (-1 * M[i][col]) / (M[row][col])

            M[i] = add_rows_coefs(M[row], coef, M[i], 1)

    return M

def backward_step(M):
    for sub in range(len(M)-1, -1, -1):
        M = back_eliminate(M, sub, sub)
        print("Adding row" , sub, "to the rows above it")
        print("The matrix is currently:\n" , M)
        print(" ")

    for row in range(len(M)):
        value = M[row][get_lead_ind(M[row])]

        for col in range(len(M[1])):
            M[row][col] /= value

    print(M)


# Problem 8 --------------------------------------------------------------------

def solve(M, b):
    M = forward_step(M)
    for i in range(len(M)):
        M[i].append(b[i])


    x = [0 for i in range(len(M))]

    for i in range(len(M)-1, -1, -1):
            x[i] = M[i][len(M)] / M[i][i]
            for k in range(i - 1, -1, -1):
                M[k][len(M)] -= M[k][i] * x[i]

    return x

if __name__ == '__main__':
    M = [[1.0, -2.0, 3.0, 22.0], [0.0, 16.0, -8.0, 248.0], [0.0, 0.0, 3.5, -38.5]]
    backward_step(M)
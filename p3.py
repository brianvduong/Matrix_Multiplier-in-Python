# Reads in 2 matrices from a text file, multiplies them together, and outputs the product.
# 10/11/19
# p3.py
# CS320
# Brian Duong

import sys

if(len(sys.argv) < 2):           #checks to see if there is no input for data
    print("Usage: p3.py dataFileName")
    sys.exit()

filename = sys.argv[1]           #sets filename to 2nd input of command line

def main():

    try:                        #returns error statement if file name is wrong
        open(filename)
    except IOError:
        print('File not found')
        sys.exit()

    if(len(sys.argv) > 2):    #checks to see if there are more than one input for data
        print("Usage: p3.py dataFileName")
        sys.exit()

    A = []
    B = []

    C = read_matrices(A, B)

    print("Program #3, cssc0474, Brian Duong")
    print("Matrix A contents:")
    print_matrix(A)
    print(" ")
    print("Matrix B contents:")
    print_matrix(B)
    print(" ")
    mult_matrices(A, B, C)
    print("Matrix A * B is:")
    print_matrix(C)


def read_matrices(A, B):
    with open(filename) as data:
        m = [int(x) for x in next(data).split()][0]     # rows of A
        n = [int(x) for x in next(data).split()][0]     # rows of B
        p = [int(x) for x in next(data).split()][0]     # cols of B

        for i in range(m):      #fills in matrix A
            A.append([int(x) for x in next(data).split()])

        for i in range(n):      #fills in matrix B
            B.append([int(x) for x in next(data).split()])

        C = [[0 for i in range(p)] for j in range(m)]       #allocates size for matrix C

        return C


def print_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])

    for rows in arr:
        for cols in rows:
            print(cols, end = ' ')
        print("")


def mult_matrices(A, B, C):
    m = len(A)
    n = len(B)
    p = len(B[0])
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

if __name__ == '__main__':
	main()

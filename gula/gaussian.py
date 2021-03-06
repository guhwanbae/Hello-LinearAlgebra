# Author  : Gu-hwan Bae
# Summary : Algorithms for solving systems of linear equations.

import numpy as np

def rowSwitchingMatrix(n, a, b):
    """
    Return a matrix which swap two rows, row a and b.
    """
    S = np.eye(n)
    temp = S[b].copy()
    S[b] = S[a]
    S[a] = temp
    return S

def rowAdditionMatrix(r, a, row_a, row_b):
    """
    Return a element addtion matrix.
    Parameter 'a' is scalar factor for multiplying.
    (e.g) Ra = Ra + a * Rb
    """
    N = np.eye(r)
    N[row_a][row_b] = a
    return N

def findNonZeroRows(M, col_idx):
    """
    Return indice of rows that an element on col_idx is non zero.
    """
    (nonzero_rows, ) = np.nonzero(M[:, col_idx])
    return nonzero_rows

def echelon(M):
    """
    Gaussian elimination algorithm, row reduction.
    Return a matrix as row echelon form.
    """
    (nrows, ncols) = M.shape
    stage = 0
    for col_idx in range(ncols):
        print('>> Iteration = %s, Stage = %d' % (col_idx, stage))
        nonzero_rows = findNonZeroRows(M[stage:], col_idx)
        nonzero_rows = nonzero_rows + stage
        print('Nonzero rows =', nonzero_rows)
        if nonzero_rows.size > 0:
            pivot = nonzero_rows[0]
            if pivot != stage:
                print('Swap R%d and R%d' % (pivot, stage))
                S = rowSwitchingMatrix(nrows, pivot, stage)
                M = np.dot(S, M)
                pivot = stage
        if nonzero_rows.size < 2:
            if nonzero_rows.size == 1:
                stage = stage + 1
            print('Skip')
            continue
        pivot_scalar = M[pivot][col_idx]
        for row_idx in nonzero_rows[1:]:
            row_scalar = M[row_idx][col_idx]
            a = -row_scalar / pivot_scalar
            N = rowAdditionMatrix(nrows, a, row_idx, pivot)
            M = np.dot(N, M)
            print('R%d = R%d + %s*R%d' % (row_idx, row_idx, a, pivot))
        stage = stage + 1
        print('M =\n', M)
    return M


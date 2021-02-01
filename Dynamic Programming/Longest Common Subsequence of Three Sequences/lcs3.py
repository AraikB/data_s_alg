# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    def lcsOf3(X, Y, Z, m, n, o):

        L = [[[0 for i in range(o+1)] for j in range(n+1)]
             for k in range(m+1)]

        ''' Following steps build L[m+1][n+1][o+1] in 
        bottom up fashion. Note that L[i][j][k] 
        contains length of LCS of X[0..i-1] and 
        Y[0..j-1] and Z[0.....k-1] '''
        for i in range(m+1):
            for j in range(n+1):
                for k in range(o+1):
                    if (i == 0 or j == 0 or k == 0):
                        L[i][j][k] = 0

                    elif (X[i-1] == Y[j-1] and
                          X[i-1] == Z[k-1]):
                        L[i][j][k] = L[i-1][j-1][k-1] + 1

                    else:
                        L[i][j][k] = max(max(L[i-1][j][k],
                        L[i][j-1][k]),
                                        L[i][j][k-1])

        # L[m][n][o] contains length of LCS for
        # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
        return L[m][n][o]
    return lcsOf3(first_sequence,second_sequence,third_sequence,len(first_sequence),len(second_sequence),len(third_sequence))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if len(A) == 0:
            return A
        for i in range(0,len(A)):
            if len(A[i]) == 0:
                continue
            for j in range(0,len(A[i])):
                if A[i][j] == 0:
                    for k in range(0,len(A)):
                        if A[k][j] == 1:
                            A[k][j] = -1
                    for m in range(0,len(A[i])):
                        if A[i][m] == 1:
                            A[i][m] = -1
        
        for i in range(0,len(A)):
            for j in range(0,len(A[i])):
                if A[i][j] == -1:
                    A[i][j] = 0
        return A

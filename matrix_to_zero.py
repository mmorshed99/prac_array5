#Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.
#
#Do it in place.
#
#Example
#
#Given array A as
#
#1 0 1
#1 1 1 
#1 1 1
#On returning, the array A should be :
#
#0 0 0
#1 0 1
#1 0 1
#Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
#
#
#Solution 1
### It doesn't use any additional space but run time is longer
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
##Solution 2
## This one uses n+m additional space but requires less time.
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if len(A) == 0:
            return A
        row = [0 for i in range(0,len(A))]
        column = [0 for i in range(0,len(A[0]))]
        for i in range(0,len(A)):
            if len(A[i]) == 0:
                continue
            for j in range(0,len(A[i])):
                if A[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
        
        for i in range(0,len(row)):
            if row[i]:
                for j in range(0,len(A[i])):
                    A[i][j] = 0
        for i in range(0,len(column)):
            if column[i]:
                for j in range(0,len(A)):
                    A[j][i] = 0
        return A

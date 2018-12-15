#You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
#
#If so, return the integer. If not, return -1.
#
#If there are multiple solutions, return any one.
#
#Example :
#
#Input : [1 2 3 1 1]
#Output : 1 
#1 occurs 3 times which is more than 5/3 times. 
####Solution source: https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        temp1 = []
        temp2 = []
        final_count = []
        for i in range(3):
            temp1.append(0)
            temp2.append(-1)
            final_count.append(0)
        for i in A:
            found_i = 0
            empty_slot = 0
            idx = -1
            for j in range(len(temp2)):
                if temp2[j] == i:
                    temp1[j] += 1
                    found_i = 1
                    break
                else:
                    if temp2[j] == -1:
                        empty_slot = 1
                        idx = j
            if found_i == 0:
                if empty_slot == 0:
                    for j in range(len(temp1)):
                        temp1[j] -= 1
                        if temp1[j] == 0:
                            temp2[j] = -1
                else:
                    temp1[idx] = 1
                    temp2[idx] = i
        done = 0
        for i in A:
            if done:
                break
            for j in range(len(temp2)):
                if i == temp2[j]:
                    final_count[j] += 1
                    if final_count[j] > len(A)// 3 :
                        return i
        return -1
####shorter###
def repeatedNumber(self, A):
        def get_numbers(A):
            max_num = {}
            for idx in range(len(A)):
                if max_num.get(A[idx]):
                    max_num[A[idx]] += 1
                    continue
                if len(max_num) < 3:
                    max_num[A[idx]] = 1
                    continue
                for each_key in max_num.keys():
                    max_num[each_key] -= 1
                    if max_num[each_key] == 0:
                        del max_num[each_key]
            return max_num
        max_num = get_numbers(A)
        for each_key in max_num.keys():
            total = 0
            for idx in range(len(A)):
                if  int(each_key) == A[idx]:
                    total += 1
                    if total > len(A)/ 3:
                        return A[idx]
        return -1

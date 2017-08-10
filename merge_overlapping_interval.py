# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        def merge_sort(A):
          new_A = []
          if len(A) == 1:
            return A
          elif len(A) == 2:
             if A[0].start > A[1].start:
                new_A.append(A[1])
                new_A.append(A[0])
             else:
                new_A = A
             return new_A
          else:     
             A_left = merge_sort(A[0:(len(A)//2)])
             A_right = merge_sort(A[len(A)//2:len(A)])
             curr_index_left = 0
             curr_index_right = 0
             while(True):
               if A_left[curr_index_left].start < A_right[curr_index_right].start :
                  new_A.append(A_left[curr_index_left])
                  curr_index_left += 1
               else:
                  new_A.append(A_right[curr_index_right])
                  curr_index_right += 1
               if curr_index_left == len(A_left) and curr_index_right == len(A_right):
                  break
               if curr_index_left == len(A_left):
                  for i in range(curr_index_right,len(A_right)):
                     new_A.append(A_right[i])
                  break
               if curr_index_right == len(A_right):
                  for i in range(curr_index_left,len(A_left)):
                     new_A.append(A_left[i])
                  break
          #print(new_A)      
          return new_A
        def combine(A):  
         #A = []
         new_A = []
         A = merge_sort(A)
         #print(A)
         if len(A) <= 1:
          return A
         new_A.append(A[0])
         if len(A)>1:
          for i in range(1,len(A)):
              temp_list = A[i]
              if temp_list.start <= new_A[-1].end and temp_list.start >= new_A[-1].start and A[i].end>=new_A[-1].end:
                  temp2 = Interval(new_A[-1].start,A[i].end)
                  new_A = new_A[:-1]
                  new_A.append(temp2)
              elif A[i].start<=new_A[-1].end and A[i].start>=new_A[-1].start and A[i].end<=new_A[-1].end: 
                  continue
              elif A[i].start> new_A[-1].end:
                  new_A.append(temp_list)
              else:
                  new_A.append(temp_list)
         return new_A
        my_A = [] 
        my_A = combine(intervals)
        newer_A = []
        while(True):
         newer_A = combine(my_A)
         if len(newer_A) == len(my_A):
             break
         else:
             my_A = newer_A
        return my_A

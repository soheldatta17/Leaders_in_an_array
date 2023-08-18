class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        arr=[A[N-1]]
        for i in range(N-2,A.index(max(A))-1,-1):
            if A[i]>=max(arr):
                arr.append(A[i])
        return arr[::-1]
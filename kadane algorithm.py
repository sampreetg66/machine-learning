   #from sys import maxint
    a=[1,2,3,-2,-1]
# Function to find the maximum contiguous subarray
#def maxSubArraySum(a,size):
      
    max_so_far = 0
    max_ending_here = 0
      
    for i in range(0, 5):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    print(max_so_far) 

# 1) Initialize a variable diff as infinite (Diff is used to store the 
#    difference between pair and x).  We need to find the minimum diff.
# 2) Initialize two index variables l and r in the given sorted array.
#        (a) Initialize first to the leftmost index in ar1:  l = 0
#        (b) Initialize second  the rightmost index in ar2:  r = n-1
# 3) Loop while  l = 0
#        (a) If  abs(ar1[l] + ar2[r] - sum) < diff  then 
#            update diff and result 
#        (b) Else if(ar1[l] + ar2[r] <  sum )  then l++
#        (c) Else r--    
# 4) Print the result. 

def closesTwoSum(ar1, ar2, x): 
  
    # Initialize the diff between  
    # pair sum and x. 
    diff=float('inf')
    m, n = len(ar1), len(ar2)
    # res_l and res_r are result  
    # indexes from ar1[] and ar2[] 
    # respectively. Start from left 
    # side of ar1[] and right side of ar2[] 
    l = 0
    r = n-1
    while(l < m and r >= 0): 
      
    # If this pair is closer to x than  
    # the previously found closest, 
    # then update res_l, res_r and diff 
        if abs(ar1[l] + ar2[r] - x) < diff: 
            res_l = l 
            res_r = r 
            diff = abs(ar1[l] + ar2[r] - x) 
      
  
    # If sum of this pair is more than x, 
    # move to smaller side 
        if ar1[l] + ar2[r] > x: 
            r=r-1
        else: # move to the greater side 
            l=l+1
    return [ar1[res_l], ar2[res_r]]     
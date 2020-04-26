from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        D=defaultdict(int)        
        for i in nums:
            D[i]+=1
        Counter=0
        for i in D:
            if D[i]>1:
                Counter+=1
        if Counter>0:
            return True
        else:
            return False

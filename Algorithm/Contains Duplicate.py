"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

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

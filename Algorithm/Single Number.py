"""
Single Number:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

from collections import defaultdict
class Solution:
    def singleNumber_v1(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

    def singleNumber_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
    
"""
Single Element in a Sorted Array:

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space
"""

from collections import defaultdict
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        Dic=defaultdict(int)
        for i  in nums:
            Dic[i]+=1
        for j in Dic:
            if Dic[j]==1:
                return j
        
        

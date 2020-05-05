"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        nums=defaultdict(int)
        for i in s:
            nums[i]+=1   
        for i in nums:
            if nums[i]==1:
                return s.index(i)
        else:
            return -1

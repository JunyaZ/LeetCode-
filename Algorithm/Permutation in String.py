"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False   
        s1Counter = Counter(s1)
        Count = Counter()
        
        for i in range(len(s2)):
            Count[s2[i]] += 1
            
            if i >= len(s1):
                if Count[s2[i-len(s1)]] == 1:
                    del Count[s2[i-len(s1)]]
                else:
                    Count[s2[i-len(s1)]] -= 1
                
            if s1Counter == Count:
                return True
            
        return False

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

   Hide Hint #1  
Obviously, brute force will result in TLE. Think of something else.
   Hide Hint #2  
How will you check whether one string is a permutation of another string?
   Hide Hint #3  
One way is to sort the string and then compare. But, Is there a better way?
   Hide Hint #4  
If one string is a permutation of another string then they must one common metric. What is that?
   Hide Hint #5  
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
   Hide Hint #6  
What about hash table? An array of size 26?

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

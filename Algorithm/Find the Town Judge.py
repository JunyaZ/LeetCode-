
from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            return 1
        else:
            score=defaultdict(int)
            for l1,l2 in trust:
                score[l1]-=1
                score[l2]+=1
            for j in score:
                if score[j]==N-1:
                    return j
            else:
                return -1
                
            
            

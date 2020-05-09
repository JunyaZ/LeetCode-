"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:


Examples2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        else:
            x1,y1=coordinates[0]
            x2,y2=coordinates[1]
            try:
                m=(y1-y2)/(x1-x2)
            except ZeroDivisionError:
                return False
            for i in range(2,len(coordinates)):
                x0,y0=coordinates[i]
                if (y0-y1)/(x0-x1)!=m:
                    return False
            else:
                return True
                

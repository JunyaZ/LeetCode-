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
                

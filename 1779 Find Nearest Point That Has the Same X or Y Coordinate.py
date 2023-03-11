class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDistance = 100000
        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance = abs(x-points[i][0]) + abs(y-points[i][1])
                if distance < minDistance:
                    minDistance = distance
                    ans = i
        return ans

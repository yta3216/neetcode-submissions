class Solution:
    def isPathCrossing(self, path: str) -> bool:
        traveled = set()
        traveled.add((0,0))

        x, y = 0, 0

        for i in path:
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            if i == 'W':
                x -= 1
            if ((x, y) in traveled):
                return True
            else:
                traveled.add((x, y))
        print(traveled)
        return False
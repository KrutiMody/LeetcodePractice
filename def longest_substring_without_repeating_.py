from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def get_neighbors(coords):
            neighbors = []
            row, col = coords
            row_offset = [-1, 0, 1, 0]
            col_offset = [0, 1, 0, -1]
            for i in range(len(row_offset)):
                rn = row + row_offset[i]
                cn = col + col_offset[i]
                if 0 <= rn < n and 0 <= cn < m:
                    neighbors.append((rn, cn))
            return neighbors
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
        while queue:
            node = queue.popleft()
            r, c = node
            for neighbor in get_neighbors(node):
                rx, cx = neighbor
                if mat[rx][cx] != 0:
                    mat[rx][cx] = mat[r][c] + 1
                    queue.append((rx,cx))
        return mat


if __name__ == '__main__':
    solution = Solution()
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = solution.updateMatrix(dungeon_map)
    for row in res:
        print(' '.join(map(str, row))) 
# solution = Solution()
# result = solution.updateMatrix([[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# print(result)
# if __name__ == '__main__':
#     solution = Solution()
#     r = int(input())
#     c = int(input())
#     replacement = int(input())
#     image = [[int(x) for x in input().split()] for _ in range(int(input()))]
#     res = solution.floodFill(image, r, c, replacement)
#     for row in res:
#         print(' '.join(map(str, row)))
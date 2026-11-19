class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board[r])):

                num = board[r][c]
                if (num == "."): continue
                b = (r // 3) * 3 + (c // 3)
                if num in rows[r] or num in cols[c] or num in box[b]:
                    return False
                else:
                    rows[r].add(num) # rows[r].add(num)
                    cols[c].add(num)
                    box[b].add(num)

        return True

# if num in rows[r] or if num in cols[c] or if num in box[b]:
    # return False

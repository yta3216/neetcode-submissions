class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for row in range(numRows):
            row = [1]

            if rows:
                last_row = rows[-1]
                
                for j in range(len(last_row) - 1):
                    row.append(last_row[j] + last_row[j + 1])
                row.append(1)
            rows.append(row)
        return rows
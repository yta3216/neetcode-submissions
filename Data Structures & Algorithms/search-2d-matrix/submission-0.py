class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_low = 0
        m_high = len(matrix) - 1
        m = 0
        found_row = False
        while m_low <= m_high and not found_row:
            m_mid = m_low + (m_high - m_low) // 2
            if (target > matrix[m_mid][-1]):
                m_low = m_mid + 1
            elif (target < matrix[m_mid][0]):
                m_high = m_mid - 1
            else:
                found_row = True
                m = m_mid
        
        if not found_row:
            return False
        
        n_low = 0
        n_high = len(matrix[m]) - 1
        while n_low <= n_high:
            n_mid = n_low + (n_high - n_low) // 2
            if (target > matrix[m][n_mid]):
                n_low = n_mid + 1
            elif (target < matrix[m][n_mid]):
                n_high = n_mid - 1
            else:
                return True
        return False

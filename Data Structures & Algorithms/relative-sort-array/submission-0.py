class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm = Counter(arr1)

        diff = list(set(arr1) - set(arr2))
        diff.sort()

        out = []

        for i in arr2:
            while hm.get(i) > 0:
                out.append(i)
                hm[i] -= 1
        for j in diff:
            while hm.get(j) > 0:
                out.append(j)
                hm[j] -= 1
        return out

        
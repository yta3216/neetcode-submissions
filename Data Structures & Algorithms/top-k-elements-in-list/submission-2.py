class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        
        largest = sorted(hm, key = hm.get)
        return largest[-k:]
        
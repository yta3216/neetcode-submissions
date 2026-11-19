class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        print(hm)
        largest = sorted(hm, key=hm.get)
        print(largest)
        return largest[-k:]
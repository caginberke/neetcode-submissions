class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for e in nums:
            counts[e] = 1 + counts.get(e, 0)

        for num, count in counts.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
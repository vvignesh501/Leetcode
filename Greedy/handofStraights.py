from collections import defaultdict
from heapq import heappop, heapify


class Solution:
    def isNStraightHand(self, hand, W: int) -> bool:

        # Check if len of hand is divisible else False
        if len(hand) % W != 0:
            return False

        n_groups = len(hand) // W

        freq = defaultdict(int)
        heap = []
        for h in hand:
            heap.append(h)
            freq[h] += 1

        heapify(heap)

        for idx in range(n_groups):
            start = heappop(heap)

            while freq[start] <= 0:
                # Understand how minHeap works here. it looks for hashMap value 0 for min
                # Start value must be 1 in 1,2,3 and 2 in 2,3,4 and 6 in 6,7,8
                # If minHeap returns 2 in 1,2,3 or 3 in 2,3,4 then return False - if freq[j] < 0
                # That j value must not be 2 in 1,2,3
                start = heappop(heap)

            for j in range(start, start + W):
                # If freq[j] don't exist it gives -1 inst
                freq[j] -= 1
                if freq[j] < 0:
                    return False
        return True


out = Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
print(out)

class Solution:
    def intervalIntersection(self, A, B):
        val = []
        i = j = 0

        while i < len(A) and j < len(B):
            
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= high:
                val.append([low, high])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return val


g = Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]]
,[[1,5],[8,12],[15,24],[25,26]])
print(g)
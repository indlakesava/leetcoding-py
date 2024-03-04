import heapq
class Solution:
    def kthSmallest(mat, k):
        heap = []
        heapq.heapify(heap)
        first_sum = sum([i[0] for i in mat])
        heapq.heappush(heap, [first_sum, [0,0,0]])

        while heap and k>1:
            cur = heapq.heappop(heap)
            for i in range(len(mat)):
                if cur[1][i]+1<len(mat[0]):
                    s = cur[0] + mat[i][cur[1][i]+1] - mat[i][cur[1][i]]
                    new_row = cur[1].copy()
                    new_row[i]+=1
                    if [s, new_row] not in heap:
                        heapq.heappush(heap, [s, new_row])
            k -= 1
        return - heapq.heappop(heap)[0]

print(Solution.kthSmallest([[1,2,7,8,10],[4,4,5,5,6],[3,3,5,6,7],[2,4,7,9,9]], 7))
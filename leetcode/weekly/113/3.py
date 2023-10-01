#  6988. 统计距离为 k 的点对  ( https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/description/ )

"""
XOR:  异或
                                    0 <= x1 XOR x2 <= k
(x1 XOR x2) + (y1 XOR y2) = k  => 
                                    0 <= y1 XOR y2 <= k

x1 XOR x2 = i  =>  y1 XOR y2 = k - i
枚举 (x2, y2) => ( x2^i, y2^(k-i) )

"""

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        cnt = Counter()
        ans = 0
        for x, y in coordinates:
            for i in range(k + 1):
                ans += cnt[x ^ i, y ^ (k - i)]
            cnt[x, y] += 1
        return ans

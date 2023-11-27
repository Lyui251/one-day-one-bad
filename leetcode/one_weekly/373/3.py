# https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        res = sorted(zip(nums, range(n)))  # 数组中值是有序的, 下标是无序的
        ans = [-1] * n

        # 分组循环
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and res[i][0] - res[i - 1][0] <= limit:
                i += 1

            idx = sorted([i for _, i in res[st: i]])  # 得到有序的下标
            for j, (x, _) in zip(idx, res[st: i]):
                ans[j] = x

        return ans
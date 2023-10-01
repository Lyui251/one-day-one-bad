# 先统计每个元素出现的个数
# 考虑出现了 c 次个数的情况:
# 1. 当 c = 1, 返回 -1
# 2. 当 c 是 3 的倍数, 那么次数加 c // 3
# 3. 当 c % 3 = 1, 则 c = (c - 4) + 4, (c - 4) 是 3 的倍数, 剩余的 4 可以用两次操作完成
# 4. 当 c % 3 = 2, 则 c = (c - 2) + 2, (c - 2) 是 3 的倍数, 剩余的 2 可以用一次操作完成
# 5. 总的来说, 都需要 (c + 2) // 3 [下取整] 次操作完成

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())

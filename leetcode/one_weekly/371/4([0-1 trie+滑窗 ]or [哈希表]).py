# https://leetcode.cn/problems/maximum-strong-pair-xor-ii/description/
# 与 421. 数组中两个数的最大异或值(https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/)
# 不同的是把 hashset 改成 hashmap，一边遍历数组，一边记录每个 key 对应的最大的 nums[i]。

# 哈希表做法
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = mask = 0

        max_bit = max(nums).bit_length() - 1
        for i in range(max_bit, -1, -1):
            mask |= 1 << i
            new_ans = ans | (1 << i)  # 当前比特位可以是 1 吗?
            d = {}  # 用 hashmap 记录

            for y in nums:
                mask_y = y & mask  # 低于 i 的比特位为 0
                if new_ans ^ mask_y in d and d[new_ans ^ mask_y] * 2 >= y:
                    ans = new_ans
                    break
                d[mask_y] = y

        return ans

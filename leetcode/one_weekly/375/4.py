"""
写法二:只记录右端点
1.遍历数组，用哈希表r记录nums[i]最右边的下标。
2.再次遍历数组，那么第一个区间就是[0, r[nums[0]]。
3.如果第二个区间和第一个区间有交集，那么合并区间，维护合并后的区间的右端点maxR。
4.如果第二个区间和第一个区间没有交集，把合并后的区间个数m加一。怎么判断没有交集? 只要第一个区间的 maxR = i 就表示没有交集。
5.返回2 ^ m-1。记得取模。


"""

MOD = 10 ** 9 + 7


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        dic = {}
        for i, x in enumerate(nums):
            dic[x] = i

        cnt = 0
        cur_i = 0
        for i, x in enumerate(nums):
            cur_i = max(cur_i, dic[x])
            if cur_i == i:
                cnt += 1

        return pow(2, cnt - 1, MOD)
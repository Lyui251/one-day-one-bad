# 2865. 美丽塔 I  [https://leetcode.cn/problems/beautiful-towers-i/description/]
"""
数据上可以暴力枚举, 每次枚举当前下标 i 作为山顶, 其中选出最大的和.
"""

# 2866. 美丽塔 II [https://leetcode.cn/problems/beautiful-towers-ii/description/]
"""
数据上不可模拟, 因此需要优化.

观察案例可以得到, 需要及时的修改/丢弃无用的数据, 因此可以想到栈; 同时山顶数组需要单调性, 因此数据结构采用单调栈.

以 i 为 山顶, 那么 ans = pre[i] + sur[i + 1], 其中 pre[i] 表示 [0 ~ i]调整后单调递增的和, sur[j] 表示 [j ~ n-1]的调整后单调递减的和.

sur 数组可通过倒序遍历, 得到调整后 下标[j ~ n-1] 的和, 同时可以设立哨兵, 以省略特判.
"""

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        st = [n]  # 哨兵
        s = 0
        sur = [0] * (n + 1)  # 数组长度 n + 1, 在后面求和时不用特判
        for i in range(n - 1, -1, -1):
            # 如果相同, 每次只保留最左的数
            # len(st) > 1, 防止特判, 方便计算数的个数
            while len(st) > 1 and maxHeights[i] <= maxHeights[st[-1]]:
                j = st.pop()
                s -= maxHeights[j] * (st[-1] - j)  # 将这一段长为 st[-1] - j 为maxHeight[j] 的值减去
            s += maxHeights[i] * (st[-1] - i)  # 更新减去的段落
            sur[i] = s
            st.append(i)
        
        ans = sur[0]    # 原数组从左到右是递减, 那么sur[0]就是答案
        
        st = [-1]  # 哨兵
        s = 0
        pre = [0] * (n + 1)
        for i in range(n):
            while len(st) > 1 and maxHeights[i] <= maxHeights[st[-1]]:
                j = st.pop()
                s -= maxHeights[j] * (j - st[-1])
            s += maxHeights[i] * (i - st[-1])
            pre[i] = s
            st.append(i)
        

        for i in range(n):
            ans = max(ans, pre[i] + sur[i + 1])
        
        return ans

# LC 556. 下一个更大元素 III:   https://leetcode.cn/problems/next-greater-element-iii/description/
# LC 31. 下一个排列:           https://leetcode.cn/problems/next-permutation/description/
"""
要让下一个更大元素尽可能地小, 那么从低位开始向高位找是最好的.
如果从低位开始向高位遍历所有数字是 非严格递增 的, 那么无法通过组合得到下一个更大元素 (如 54321)

在找到 第一个递减的下标 idx 时, 从低位开始遍历找到第一个大于 s[idx] 的数字 s[j],
交换 s[idx] 和 s[j] 后, 因为需要使下一个更大元素尽可能小, 还需要对 s[idx+1:] 进行反转;
因为在倒序遍历时, s[idx+1:] 符合 非严格递减(倒过来是 非严格递增),
那么需要通过反转使 s[idx+1:] 符合 非严格递增
"""
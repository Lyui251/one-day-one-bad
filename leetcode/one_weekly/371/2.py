# https://leetcode.cn/problems/high-access-employees/description/
"""
把名字相同的员工对应的访问时间（转成分钟数）分到同一组中。

对于每一组的访问时间 a，排序后，判断是否有 a[i]−a[i−2]<60，如果有，那么把这一组的员工名字加到答案中。
"""
from collections import defaultdict
from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        p = defaultdict(list)
        for a, tt in access_times:
            t = int(tt[:2]) * 60 + int(tt[2:])  # 转换成分钟
            p[a].append(t)

        ans = []
        for k, t in p.items():
            t.sort()
            if any(t[i] - t[i - 2] < 60 for i in range(2, len(t))):
                ans.append(k)

        return ans

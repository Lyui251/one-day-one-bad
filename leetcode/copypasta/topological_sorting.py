# 拓扑排序

"""
反向图 + 拓扑排序
LC:   [802. 找到最终的安全状态]
      题意:  给定一个有向无环图, 要求找到所有的点, 该点的所有可能路径都不会形成一个环
      
      如果想要判断某个节点 x 是否为安全节点, 起始时将 x 加入队列, 并跑一遍拓扑排序是不够的.
      因为我们无法实现保证 x 满足入度为 0 的条件, 所以当我们处理到与 x 相连的节点 y 时, 可能会存在
      y 节点入度无法减到 0 的情况---即我们无法输出真实拓扑序中, 从 x 节点开始到结尾的完整部分.
      但如果将所有边反向, 这时节点的 入度 和 出度 就翻转了.
      
      根据题意，若一个节点没有出边，则该节点是安全的；若一个节点出边相连的点都是安全的，则该节点也是安全的。
      根据这一性质，我们可以将图中所有边反向，得到一个反图，然后在反图上运行拓扑排序。
      具体来说，首先得到反图 rg 及其入度数组 Deg。将所有入度为 0 的点加入队列，然后不断取出队首元素，
      将其出边相连的点的入度减一，若该点入度减一后为 0，则将该点加入队列，如此循环直至队列为空。
      循环结束后，所有入度为 0 的节点均为安全的。我们遍历入度数组，并将入度为 0 的点加入答案列表。
"""

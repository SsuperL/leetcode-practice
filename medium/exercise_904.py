"""
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        max_len = 1
        l = []  # l最大长度为2
        for j in range(len(fruits)):
            if fruits[j] not in l:
                if len(l) >= 2:
                    # 去掉最早加入的元素
                    l.remove(l[0])
                    # j的前一个元素必须要与l中的第一个元素一致，否则l[0]是较早加入的元素
                    if fruits[j - 1] != l[0]:
                        l[0] = fruits[j - 1]
                    l.append(fruits[j])
                    i = j - 1
                    while i >= 0:
                        # 从j-1开始从后往前遍历，遇到第一个不等于l[0]的元素结束遍历
                        if fruits[i] != l[0]:
                            i += 1
                            break
                        i -= 1
                else:
                    l.append(fruits[j])
            max_len = max(max_len, j - i + 1)

        # return max_len
        print(max_len)


solution = Solution()
# solution.totalFruit([0,1,2,2])
# solution.totalFruit([1,0,0,0,1,0,4,0,4])
# solution.totalFruit([1,1,0,0,1,5,5,6])
# solution.totalFruit([4,1,1,1,3,1,7,5])
# solution.totalFruit([1,2,1])
# solution.totalFruit([1,2,3,2,2])
# solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
# solution.totalFruit([0,1,2,2])
# solution.totalFruit([0,1,6,6,4,4,6])
# solution.totalFruit([1,2])
# solution.totalFruit([0,1,0,2])
# solution.totalFruit([0,1,6,6,4,4,6])
solution.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3])

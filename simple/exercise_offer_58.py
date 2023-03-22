"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 方法一
        s_list = list(s)
        left = 0
        right = len(s_list)
        s_list.extend([" "] * n)
        while left < n:
            s_list[right] = s_list[left]
            left += 1
            right += 1
        return "".join(s_list[n:])
        # 方法二：不申请额外空间，先反转前 n 的子串，在反转 区间 n到末尾到子串，最后反转整个字符串


solution = Solution()
print(solution.reverseLeftWords("abcdefg", 2))

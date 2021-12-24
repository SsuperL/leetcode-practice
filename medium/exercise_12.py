"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
             9: "IX", 4: "IV", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        s = ''
        while num != 0:
            if num//1000 > 0:
                s += num//1000*d[1000]
                num = num-1000*(num//1000)
            if num//100 > 0:
                # 特殊情况，400，900
                if num//100 < 5:
                    if num//100 == 4:
                        s += d[400]
                    else:
                        s += num//100*d[100]
                else:
                    if num//100 == 9:
                        s += d[900]
                    else:
                        s += d[500]+(num-500)//100*d[100]
                num = num-100*(num//100)
            if num//10 > 0:
                if num < 50:
                    if num//10 == 4:
                        s += d[40]
                    else:
                        s += num//10*d[10]
                else:
                    if num//10 == 9:
                        s += d[90]
                    else:
                        s += d[50]+(num-50)//10*d[10]
                num = num-10*(num//10)
            else:
                if num < 5:
                    if num == 4:
                        s += d[4]
                    else:
                        s += num*d[1]
                else:
                    if num == 9:
                        s += d[9]
                    else:
                        s += d[5]+(num-5)*d[1]
                num = 0
        return s


solution = Solution()
print(solution.intToRoman(58))

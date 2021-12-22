'''
将字符串按z形排列并按行输出
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        for i in range(len(s)):
            i, flag = 0, -1
            res = ["" for i in range(numRows)]
            for v in s:
                res[i] += v
                if i == 0 or i == numRows-1:
                    # 反向
                    flag = -flag
                i += flag
        return "".join(res)


solution = Solution()
print(solution.convert("ibgkxinzlgbjntwrvtlbmstfemisdnslpavokkovqphekfxiaijmaeugqcbtrvggvdxfnlcdajjnqgvqpedrizaabbtswbbteyatlcwnoiaeovvdbaxlzxlcygwwhzpnzpgkrfahnambyjhzlelkbwobfkxmkmcjbiwupwccwqguznwmrhyufmvkyszigbuhlsdbofdmxjjyyfkroiltuievcffigzrtrvuhcaucldakkldyvprszxnecsmkugendavhapjmukyexdcsutmutzyvumiosmbxmwfpnodhadnxgpsblevegvbahlqcxrzmqebfvgpvjcvpupqfvnlbiodsatuznvldcoixuxudcpvwelbcbodjejdecxgpttuviduecokeefaksdottsfabigfgmxbgryqusuziefojibcnpvjhcjklpstcpuiguydouewzjlkrmmhbkqlmzxzopssgmcnicswxwtwheibqvithyevzevptnicckpknjhmhakogspypzrwxyuycpoxewzgiqtxzcjgetxkmm", 343))

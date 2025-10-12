# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1) + int(num2))

        res_str = ""
        carry   = 0
        l1 = len(num1)
        l2 = len(num2)
        if l1 >= l2:
            largenum = num1
            shortnum = num2
            largestrlen = l1
            shortstrlen = l2
        else:
            largenum = num2
            shortnum = num1
            largestrlen = l2
            shortstrlen = l1
        p_large = largestrlen - 1
        p_short = shortstrlen - 1

        temp_result_digits_list = []

        while p_large >= 0 or carry:

            digit_large = 0
            if p_large >= 0:
                digit_large = ord(largenum[p_large]) - ord('0')
                p_large -= 1
            
            digit_short = 0
            if p_short >= 0:
                digit_short = ord(shortnum[p_short]) - ord('0')
                p_short -= 1

            current_sum = digit_large + digit_short + carry

            temp_result_digits_list.append(str(current_sum % 10))

            carry = current_sum // 10
        res_str = "".join(temp_result_digits_list[::-1])
        return res_str

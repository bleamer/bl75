#lc-537 Complex Number Multiplication

import re
class Solution:
    def parse_num(self, num: str):
        exp = r"([+-]?\d*)\.*\+([-]?\d*)i"
        print(num)
        match = re.match(exp, num.strip())
        if match:
            real = int(match.group(1))
            im = int(match.group(2))

        if real: print(real)
        if im: print(im)
        return real,im

    def multiply_complex(self, n1, n2):
        print(n1, n2)
        real = n1[0]*n2[0] - n1[1] * n2[1]
        im = n1[0]*n2[1] + n1[1] * n2[0]
        return real, im

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1 = self.parse_num(num1)
        n2 = self.parse_num(num2)

        res = self.multiply_complex(n1, n2)
        return f"{res[0]}+{res[1]}i"
        

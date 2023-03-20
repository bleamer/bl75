# LC-68-Text Justification
# https://leetcode.com/problems/text-justification/description/
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        n = len(words)
        i = 0
        sep = " "
        while i < n:
            line =[]
            line_len =0
            
            while i < n and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1
            rem_sep = maxWidth - line_len
            if i == n or len(line) == 1:
                line_str = sep.join(line)
                result.append(line_str + " "*(maxWidth - len(line_str)))
            else:
                spaces_per_gap = rem_sep // (len(line)-1)
                extra_spaces = rem_sep % (len(line)-1)
                line_str = ""
                for k, word in enumerate(line):                
                    line_str += word
                    if not k == len(line)-1:
                        line_str += sep*(spaces_per_gap + ( k < extra_spaces))
                result.append(line_str)
            # print(result)
        return result
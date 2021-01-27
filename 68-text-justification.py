from typing import List

class Solution:
    def make_line(self, st, maxWidth, buffer):
        if len(st) == 1:
            return st[0] + " "*(maxWidth-buffer)
        space_length = (maxWidth - buffer) // (len(st)-1)
        spaces = maxWidth - buffer - space_length*(len(st)-1)
        result = []
        # print(st, space_length, spaces)
        for i,w in enumerate(st):
            result.append(w)
            if i == len(st)-1:
                break
            elif i < spaces:
                result.append(' '*(space_length+2))
            else:
                result.append(' '*(space_length+1))
        return "".join(result)
    def make_last_line(self, st, maxWidth):
        result = " ".join(st)
        remainder = maxWidth - len(result)
        result = result + " "*remainder
        return result

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buffer = 0
        st = []
        result = []
        for i,w in enumerate(words):
            if not buffer:
                buffer = len(w)
                st.append(w)
            elif (buffer + 1 + len(w) <= maxWidth):
                st.append(w)
                buffer += len(w) + 1
            else:
                result.append(self.make_line(st, maxWidth, buffer))
                buffer = len(w)
                st = [w]
        if st:
            result.append(self.make_last_line(st, maxWidth))

        return result


sol = Solution()
test_cases = [
[["This", "is", "an", "example", "of", "text", "justification."], 16], #3
[["What","must","be","acknowledgment","shall","be"], 16], #5
[["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20], #6
[["single_word"], 50],
[["a","b","c"],1],
]
for t in test_cases:
    print(t, sol.fullJustify(t[0],t[1]))

"""
spaces = number of words - 1
total = total chars + spaces

once we overfill, start making string
    fill right to left, spaces = maxWidth - totalchars - required_spaces // (number of words - 1)
        start filling
    if we have remaining spaces, which <= number of words - 1
    remaining spaces can be found using mod, one easy way is to create an array to hold spaces count,
    or just count the number of +1 spaces spots

start building stack again, reset stack, reset buffer

end of line is special case:
    fill left to right, join, then add remaining spaces to fit the word


"""

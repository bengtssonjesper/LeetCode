# Runtime: 24 ms, faster than 96.06% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        openOrder = []
        index = 0
        for i in s:
            if i == "(":
                openOrder.append(1)
                index += 1
            elif i == "[":
                openOrder.append(2)
                index += 1
            elif i == "{":
                openOrder.append(3)
                index += 1
            elif i == ")" and index > 0:
                if openOrder[index-1] == 1:
                    del openOrder[-1]
                    index -= 1
                else:
                    return False
            elif i == "]" and index > 0:
                if openOrder[index-1] == 2:
                    del openOrder[-1]
                    index -= 1
                else:
                    return False
            elif i == "}" and index > 0:
                if openOrder[index-1] == 3:
                    del openOrder[-1]
                    index -= 1
                else:
                    return False
            else:
                return False
        if len(openOrder) == 0:
            return True
        else:
            return False

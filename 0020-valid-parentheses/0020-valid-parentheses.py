class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        bracket = ""
        for i in range(0, len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                brackets.append(s[i])
            else:
                if len(brackets)>0:
                    elem = brackets.pop()
                    if s[i] == ")":
                        if elem != "(":
                            return False
                    elif s[i] == "}":
                        if elem != "{":
                            return False
                    else:
                        if elem != "[":
                            return False
                else:
                    return False
        if len(brackets) == 0:
            return True
        return False
        

        
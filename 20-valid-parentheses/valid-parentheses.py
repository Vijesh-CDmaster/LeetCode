class Solution(object):

    def isValid(self, s):

        stack = []

        for i in s:

            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            else:
                if not stack:
                    return False

                x = stack.pop()

                if i == ')' and x != '(':
                    return False

                if i == ']' and x != '[':
                    return False

                if i == '}' and x != '{':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
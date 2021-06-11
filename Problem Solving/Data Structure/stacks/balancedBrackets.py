s = input()

stack = []

openBrackets = ["{","[","("]
closeBrackets = ["}","]",")"]

isBalance = True

for i in range(len(s)):

    if s[i] in openBrackets:
        stack.append(s[i])

    else:
        try:
            temp = stack.pop()
        except:
            isBalance = False
            break
        if s[i] == "}":
            if temp != "{":
                isBalance = False
                break

        if s[i] == "]":
            if temp != "[":
                isBalance = False
                break

        if s[i] == ")":
            if temp != "(":
                isBalance = False
                break




print(isBalance and len(stack) > 1)













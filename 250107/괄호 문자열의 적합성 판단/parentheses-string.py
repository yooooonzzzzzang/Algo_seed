strs = input()
stack = []
# Write your code here!
for i in strs:
    if i == "(":
        stack.append("(")
    else:
        if not stack:
            print("No")
            exit(0)
        else:
            stack.pop()
if stack:
    print("No")
else:
    print("Yes")
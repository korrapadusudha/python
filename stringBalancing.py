open_list = ["[","{","("]
close_list = ["]","}",")"]
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
                print("len",len(stack))
                print("is",open_list[pos])
                print(["to",len(stack)-1])
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
# Driver code
mystr = input("enter string")
print(mystr,"-", check(mystr))
  

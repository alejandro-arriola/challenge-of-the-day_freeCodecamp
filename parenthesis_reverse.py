** start of main.py **

def decode(s):
    stack = []
    decoded = []

    for char in s:
        #print(stack, decoded)

        if char != ')':
            stack.append(char)
        else:
            while stack[-1] and stack[-1] != '(':
                decoded.append(stack.pop())
                #print(stack, decoded)
            stack.pop()
            #print(stack, decoded)
            stack.extend(decoded)
            #print(stack, decoded)
            decoded.clear()
            #print(stack, decoded)
            
    return "".join(stack)

print(decode("(f(b(dc)e)a)"))

** end of main.py **


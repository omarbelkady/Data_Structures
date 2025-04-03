# Stack implementation using a list
def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    if stack:
        return stack.pop()
    return None

def peek(stack):
    return stack[-1] if stack else None

def is_empty(stack):
    return len(stack) == 0

def infix_to_postfix(infix_expr):
                 
    precedence = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    postfix = []
    
    for char in infix_expr:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        else:
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)

def postfix_to_infix(postfix_expr):
    """
    Converts a postfix expression (e.g., "ABC*+") to infix notation (e.g., "(A+(B*C))").
    Adds parentheses to preserve evaluation order.
    """
    stack = []
    operators = {'+', '-', '*', '/', '^'}
    
    for token in postfix_expr.split():
        if token not in operators:
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expr = f"({operand1}{token}{operand2})"
            stack.append(expr)
    
    return stack.pop()


infix = "A+B*(C^D-E)^(F+G*H)-I"
postfix = infix_to_postfix(infix)

# Example Usage:
stack = []
push(stack, 10)  # [10]
push(stack, 20)  # [10, 20]
pop(stack)       # Returns 20 → stack [10]
peek(stack)      # Returns 10
print(postfix)

postfix="A B C D ^ E - F G H * + ^ * + I -"

infix = postfix_to_infix(postfix)
print(infix)  



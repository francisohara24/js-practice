# Function returns True if balanced, False otherwise.
from collections import deque


def is_balanced(s: str) -> bool:
    """Function to find whether all parentheses in a given string are balanced"""
    stack = deque()
    for c in s:
        if c == "(":
            stack.appendleft(c)
        elif c == ")":
            if len(stack) > 0:
                stack.popleft()
            else:
                return False

    if len(stack) > 0:
        return False
    else:
        return True


print(is_balanced("((())())"))

def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()(")
        False

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False
    """
    count = 0
    for s in parens:
        if s == "(":
            count +=1
        elif s==")":
            count -=1
        
        if count <0:
            return False
    
    return count ==0
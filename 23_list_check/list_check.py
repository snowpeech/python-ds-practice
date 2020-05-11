def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    
# if instanceof val,list =true is false return False
    #create a instanceof array 
    for value in lst:
        if not isinstance(value,list):
            return False
    return True

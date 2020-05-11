def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # for num in range. divide. check if answer is int. if int. add to list. return sorted list
    # to check if int.. round and see if they're equal?
    factors=[]
    for value in list(range(1,int(num/2))):
        if (num/value) == round(num/value):
            factors.append(value)
            factors.append(round(num/value))
    print("!",factors)
    return factors.sort()

find_factors(10)
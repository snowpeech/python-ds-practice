def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy = []
    for thing in lst:
        if thing:
            truthy.append(thing)

    return truthy

    # return [val for val in lst if val]
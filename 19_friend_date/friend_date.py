def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False

    #I misread the question TWICE
    # a_list = []
    # for adj in a:
    #     if isinstance(adj, list):
    #         for item in adj:
    #             a_list.append(item)
    #     else:
    #         a_list.append(adj)

    # b_list=[]
    # for adj in b:
    #     if isinstance(adj, list):
    #         for item in adj:
    #             b_list.append(item)
    #     else:
    #         b_list.append(adj)
    # print(a_list)
    # print(b_list)
    # for adj in a_list:
    #     if adj in b_list:
    #         return True
        
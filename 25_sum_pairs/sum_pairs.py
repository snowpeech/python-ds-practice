def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.
    For example:
        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)
    (4, 2) sum to 6, and come before (5, 1):
        >>> sum_pairs([4, 2, 10, 5, 1], 6) 
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):
        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)
    No pairs sum to 100, so return empty tuple:
        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    pair1 ={}
    # pair2 =() store index as third value of pair?
    #we're looking to see that the indexes of the pair are less than the max. - store the greater index and make sure they're both smaller than that...stored pair will be the y ind.
    indx = 1
    for x in nums:
        nums2 = nums[indx::1]
        indx+=1
        for y in nums2:
            if x + y == goal:
                if not pair1:
                    pair1={"pair":(x,y), "indx":nums.index(y)}
                elif nums.index(y) < pair1["indx"]:
                    pair1={"pair":(x,y), "indx":nums.index(y)}     
    if not pair1:
        return ()
    return pair1["pair"]
                

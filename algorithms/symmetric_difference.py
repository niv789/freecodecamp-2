def sym(arg1, *argv):
    
    """
    returns the symmetric difference of two or more arrays
    
    """
    x = set(arg1)
    for lst in argv:
        x.symmetric_difference_update(lst)
    return list(x)

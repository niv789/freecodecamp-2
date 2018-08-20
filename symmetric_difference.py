def sym(arg1, *argv):
    
    """
    returns the symmetric difference of two or more arrays
    
    """
    x = []
    list = arg1.copy()
    x = arg1.copy()
    for lst in argv:
        for item in lst:
            if item in x and item in lst:
                x.remove(item)
                continue
            if item in x:
                continue
            if item not in list:
                x.append(item)
    return x


A = [1,2,3]
B = [5,2,1,4]
C = [3,8]
D = [5,10]
E = [11,8,10]
x = sym(A,B,C,D,E)
print(x)
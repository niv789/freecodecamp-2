def pairwise(arr, arg):
    lst_ = []
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1, l):
            if chksum(arr[i], arr[j], arg) and i not in lst_ and j not in lst_:
                lst_.append(i)
                lst_.append(j)
    return sum(lst_)


def chksum(a, b, arg):
    if a+b == arg:
        return True
    return False

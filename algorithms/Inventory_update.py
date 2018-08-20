def updateInventory(invn, new):
    count = 0
    for item in new:
        for exis_ in invn:
            if item[1] == exis_[1]:
                exis_[0] = exis_[0] + item[0]
                new.remove(item)
    if len(new) != 0:
        for item in new:
            invn.append(item)
    return sorted(invn, key=lambda x: x[1])

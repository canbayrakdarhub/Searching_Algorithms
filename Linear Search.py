

"""Linear Search"""

def linear_search(list,target):

    for i in range(0,len(list)):
        if list[i] == target:
            return i
    else:
        return None


def verify(index):
    if index is not None:
        print("The target is in the index:", index)
    else:
        print("The target is not in the list")


list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

result = linear_search(list1,8)
verify(result)

result2 = linear_search(list1, 31)
verify(result2)



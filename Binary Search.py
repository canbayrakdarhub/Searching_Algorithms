

def binary_search(list,target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first = midpoint+1

        elif list[midpoint] > target:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("The target is in the index:", index)
    else:
        print("The target is not in the list")

list1= [0,1,2,3,4,5,6,7,8,9,10]
#Has to be sorted otherwise it won't work


result = binary_search(list1,8)
verify(result)






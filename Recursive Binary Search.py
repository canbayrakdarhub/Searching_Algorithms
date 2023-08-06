
def recursive_binary_search(list,target):

    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint-1],target)


def verify(result):
    if result == True:
        print("TRUE, The number is in the list.")
    else:
        print("FALSE, The number is not in the list.")



list1= [0,1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(list1,8)

verify(result)

result = recursive_binary_search(list1,12)

verify(result)




from typing import List

def find_target_index(array: List[int], target) -> int:
    elementIndex: int = 0
    n = int(len(array) / 2)
    array_one, array_two = array[ :n], array[n: ]
    if target in array_one:
        elementIndex = array_one.index(target) + n
    elif target in array_two:
        elementIndex = array_two.index(target) + n
    else:
        elementIndex =  -1
    return elementIndex


print(find_target_index([1,2,3,4,5,6,7,8], target=8))
print(find_target_index([1,2,3,4,5,6,7,8], target=100))

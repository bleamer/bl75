# Merge sort implementation

from typing import List


def mergeList(leftList, rightList):
    lidx, ridx = 0,0
    merged = []
    while lidx < len(leftList) and ridx < len(rightList):
        if leftList[lidx] < rightList[ridx]:
            merged.append(leftList[lidx])
            lidx +=1
        else:
            merged.append(rightList[ridx])
            ridx += 1
    merged += leftList[lidx:]
    merged += rightList[ridx:]
    return merged




def mergeSort(inp:List) -> List:
    if len(inp) <= 1:
        return inp

    mid = int(len(inp)/2)
    llist = mergeSort(inp[:mid])
    rlist = mergeSort(inp[mid:])
    return mergeList(llist, rlist)




if __name__ == '__main__':
    org_list = [34,534534,53,64557,678,867,867,6345]
    print(f'\nGiven list: {org_list}')
    print(f'Sorted list: {mergeSort(org_list)}\n')
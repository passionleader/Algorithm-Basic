"""
최악 및 최선의 시간복잡도
logn번 쪼개기  * n번 비교하기 => O(nlogn)

특징
본인이 본인을 호출하는 재귀적 구조
이진 트리만큼 반으로 쪼갠다  (log n)
*
최대 n번 비교 및 합친다  (n)
"""


# Merge Sort (divide and sort-merge)
def mergeSort(unsorted):
    # don't need to sort
    if len(unsorted) <= 1:
        return unsorted

    # divide
    LL = unsorted[:len(unsorted)//2]
    RL = unsorted[len(unsorted)//2:]

    # recurrence call and sort-merge
    return merge(mergeSort(LL), mergeSort(RL))


# Merge (sort & merge)
def merge(L, R):
    Lcount = 0  # ASC: append from left, not right
    Rcount = 0  # 좌측부터 뺴야지 오름차순으로 정렬이 됨
    sorted_list = []
    print(L, R, end='->')

    # compare and merge to new list "sorted"
    while (Lcount < len(L)) & (Rcount < len(R)):  # 하나라도 다 돌면 quit, 괄호 조심
        # Ascending
        if L[Lcount] < R[Rcount]:
            sorted_list.append(L[Lcount])
            Lcount += 1
        elif L[Lcount] > R[Rcount]:
            sorted_list.append(R[Rcount])
            Rcount += 1
        else:  # L[Lcount] == R[Rcount]
            sorted_list.append(R[Rcount])  # append to anywhere
            Rcount += 1

    # 찌꺼기 append (큰게 몰빵되어서 compare 하지 못한 찌꺼기들을 append)
    while Lcount < len(L):
        sorted_list.append(L[Lcount])
        Lcount += 1
    
    while Rcount < len(R):
        sorted_list.append(R[Rcount])
        Rcount += 1

    print(sorted_list)
    return sorted_list


LS = [7, 6, 2, 251, 23, 66, 5, 53]
n = len(LS)
print(LS)

# print(L[:len(L)//2], low, high, L[len(L)//2:])
result = mergeSort(LS)
# print(result)

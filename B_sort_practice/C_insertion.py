"""
최악의 경우 시간복잡도
n^2번의 비교 + n^2번의 교환
상수는 무시 => O(n^2)

최선의 경우 시간복잡도
n번의 비교 + 1번의 교환
상수는 무시 => O(n)

공간복잡도
swap 에 필요한 변수 => 상수
O(1) => 크기 n의 array 포함 O(n)

비교해서 삽입함(일부 shift 필요)
oo###
#oo##
o#o##
##oo#
#o#o#
o##o#
(현재 인덱스까지는 정렬되어 있음을 보장해 줌, 최선의 경우 O(n))
"""

L = [7,6,2,25,23,66,5,53]
n = len(L)
print(L)

for last in range(1, n):
    insert_index = last  # initialize
    key = L[last]  # compare & insert this!

    # insert 될 index 찾기
    for arr in range(last, 0, -1):
        if key < L[arr - 1]:
            insert_index = arr - 1  # insertable index
            # L[arr+1] = L[arr]  # shift for insert => 이해를 돕기 위해 이동 및 삽입은 하단에 반복문 분리
    print('{} -> ({})'.format(key, insert_index))

    # 이동 및 삽입
    for arr in range(last, insert_index, -1):
        L[arr] = L[arr-1]
    L[insert_index] = key

    print(L)
    
    
# # 정석
# for last in range(1, n):
#     for arr in range(last, 0, -1):
#         if L[arr - 1] > L[arr]:
#             L[arr - 1], L[arr] = L[arr], L[arr - 1]
# print(L)


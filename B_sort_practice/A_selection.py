"""
최악의 경우 시간복잡도
n^2번의 비교 + n번의 교환
상수는 무시 => O(n^2)

최선의 경우 시간복잡도
n^2번의 비교 + 1번의 교환
상수는 무시 => O(n^2)

공간복잡도
swap 에 필요한 2개의 변수 => 상수
O(1) => 크기 n의 array 포함 O(n)

순차적으로 비교해 바꿈
oo###
o#o##
o##o#
o###o
#oo##
"""

L = [1,6,2,25,23,66,5,53]
n = len(L)
print(L)

for i in range(0, n-1):
    for j in range(i+1, n):
        # 비교 + 교환
        if L[i] > L[j]:
            tmp = L[i]
            L[i] = L[j]
            L[j] = tmp

    print('->', L)

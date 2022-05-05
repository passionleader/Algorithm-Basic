"""
최악의 경우 시간복잡도
n^2번의 비교 + n^2번의 교환
상수는 무시 => O(n^2)

최선의 경우 시간복잡도
n번의 비교 + 1번의 교환
상수는 무시 => O(n)

공간복잡도
swap 에 필요한 2개의 변수 => 상수
O(1) => 크기 n의 array 포함 O(n)

큰걸 하나씩 뒤로 보냄(바꿈)
oo###
#oo##
##oo#
###oo
oo###
"""

L = [1,6,2,25,23,66,5,53]
n = len(L)
print(L)

for i in range(n-1, 0, -1):
    for j in range(0, i):
        # 비교 + 교환
        if L[j] > L[j+1]:
            tmp = L[j+1]
            L[j+1] = L[j]
            L[j] = tmp

    print('->', L)

"""
최악의 경우 시간복잡도
nlogn 번의 비교 + n^2 번의 교환
상수는 무시 => 검색 시간은 줄였지만 여전히 O(n^2)

최선의 경우 시간복잡도
nlogn 번의 비교 + 1번의 교환
상수는 무시 => O(n)

공간복잡도
swap 에 필요한 변수 => 상수
O(1) + 크기 n의 array => O(n)

전과 동일,
단 비교 시 이진 검색으로 찾는다
"""

L = [7,6,2,25,23,66,5,53]
n = len(L)
print(L)

for last in range(1, n):
    key = L[last]  # compare & insert this!

    # insert 될 index 찾기
    low = 0
    high = last
    while low < high:
        mid = (low + high) // 2
        # 키값에 따른 처리
        if key < L[mid]:  # 키가 중간값보다 작음, 초반부에 넣어야 함
            high = mid  # 더 자세한 위치 검색
        elif L[mid] < key:  # 키가 중간값 보다 큼, 후반부에 넣어야 함
            low = mid + 1  # 다음 구간으로 이동해서 검색
        elif L[mid] == key:  # 키가 중간값과 동일할 경우, 마찬가지로 뒤로 뻄
            low = mid + 1  # 다음 구간으로 이동해서 검색
    insert_index = low
    print(key, '->', insert_index)

    # 이동 및 삽입
    for arr in range(last, insert_index, -1):
        L[arr] = L[arr-1]
    L[insert_index] = key

    print(L)

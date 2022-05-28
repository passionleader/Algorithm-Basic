# 최악의 경우에도 이진 트리만큼 걸림 (반으로 무한정 쪼갬)
# O(logn)

L = [90, 15, 2, 28, 6, 8, 22, 6, 11, 14, 33]
key = 8

low = 0
high = len(L) - 1

while low < high:
    mid = (low + high) // 2
    if key < L[mid]:  # 키 값이 왼쪽에 있으면 왼쪽 심층탐색
        high = mid
    elif key > L[mid]:  # 키 값이 오른쪽에 있으면 오른쪽 심층탐색
        low = mid + 1
    elif key == L[mid]:
        print('index', mid)
        quit()


# worst case O(n)

L = [90, 15, 2, 28, 6, 8, 22, 6, 11, 14, 33]
key = 14

for i in range (len(L)):
    if L[i] == key:
        print('index', i)
        quit()
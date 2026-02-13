import sys; sys.stdin = open('도로건설.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split)) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            pass
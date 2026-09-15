def add_square_matrix(a, b):

    n = len(a)
    #두 행렬의 행 개수 확인
    if n == 0 or len(b) != n:
        raise ValueError("두 행렬은 같은 크기여야 합니다.")

    #각 행의 개수가 n 개 인지 확인 : n*n 행렬인지 확인
    if any(len(row) != n for row in a):
        raise ValueError("a는 정방행렬이야 합니다.")

    if any(len(row) != n for row in b):
        raise ValueError("b는 a와 같은 크기의 정방행렬이여야 랍니다.")

    #결과를 저장 할 n*n 행렬 0으로 초기화
    c = [[0 for _ in range(n)] for _ in range(n)]

    #같은 위치의 원소끼지 덧셈
    for i in range(n): 
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c

# 두 행렬 방향 정의

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6], 
    [7, 8]
]

c = add_square_matrix(a, b)

# 결과 출력
print("행렬 a + b = ")
for row in c:
    print(row)

# A: 4행 3열 행렬
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# B: 3행 2열 행렬
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# 행렬의 크기
rows_a = len(A)        # A의 행 개수: 4
cols_a = len(A[0])     # A의 열 개수: 3
rows_b = len(B)        # B의 행 개수: 3
cols_b = len(B[0])     # B의 열 개수: 2

# 행렬 곱셈 가능 여부 확인
if cols_a != rows_b:
    raise ValueError("A의 열 개수와 B의 행 개수가 같아야 합니다.")

# 결과 행렬 C: 4행 2열, 모든 원소를 0으로 초기화
C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

# 행렬 곱셈
for i in range(rows_a):            # A의 행 선택
    for j in range(cols_b):        # B의 열 선택
        for k in range(cols_a):    # 대응하는 원소끼리 곱하여 누적
            C[i][j] += A[i][k] * B[k][j]

# 결과 출력
print("행렬 A * B = ")
for row in C:
    print(row)
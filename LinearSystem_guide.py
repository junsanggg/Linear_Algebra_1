import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. 벡터 정의
# -------------------------------------------------
zero = np.array([0, 0, 0])

a1 = np.array([2, 3, 1])
a2 = np.array([1, 4, 2])

# 벡터의 합과 선형결합
a1_plus_a2 = a1 + a2
two_a1 = 2 * a1
combination = 2 * a1 + a2

# -------------------------------------------------
# 2. 평면의 법선벡터 계산
# -------------------------------------------------
normal_vector = np.cross(a1, a2)

print("영벡터 =", zero)
print("a1 =", a1)
print("a2 =", a2)

print("\na1 + a2 =", a1_plus_a2)
print("2a1 =", two_a1)
print("2a1 + a2 =", combination)

print("\na1 × a2 =", normal_vector)
print(
    f"평면 방정식: "
    f"{normal_vector[0]}x "
    f"{normal_vector[1]:+}y "
    f"{normal_vector[2]:+}z = 0"
)

# -------------------------------------------------
# 3. 3차원 그래프 설정
# -------------------------------------------------
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection="3d")


# 벡터를 그리는 함수
def draw_vector(vector, color, label, start=zero,
                linewidth=2.5, alpha=1.0):

    ax.quiver(
        start[0], start[1], start[2],
        vector[0], vector[1], vector[2],
        color=color,
        linewidth=linewidth,
        arrow_length_ratio=0.08,
        alpha=alpha
    )

    end = start + vector

    ax.text(
        end[0], end[1], end[2],
        f"  {label}\n  {tuple(end)}",
        color=color,
        fontsize=10
    )


# -------------------------------------------------
# 4. 기본 벡터 그리기
# -------------------------------------------------
draw_vector(a1, "blue", r"$a_1$")
draw_vector(a2, "orange", r"$a_2$")

# 벡터의 합
draw_vector(
    a1_plus_a2,
    "green",
    r"$a_1+a_2$"
)

# 스칼라곱
draw_vector(
    two_a1,
    "purple",
    r"$2a_1$"
)

# 최종 선형결합
draw_vector(
    combination,
    "red",
    r"$2a_1+a_2$",
    linewidth=3.5
)

# -------------------------------------------------
# 5. 벡터 덧셈의 이동 과정 표시
# -------------------------------------------------

# a1의 끝에서 a2만큼 이동
ax.plot(
    [a1[0], a1_plus_a2[0]],
    [a1[1], a1_plus_a2[1]],
    [a1[2], a1_plus_a2[2]],
    linestyle="--",
    color="orange",
    linewidth=2
)

# 2a1의 끝에서 a2만큼 이동
ax.plot(
    [two_a1[0], combination[0]],
    [two_a1[1], combination[1]],
    [two_a1[2], combination[2]],
    linestyle="--",
    color="orange",
    linewidth=2
)

# -------------------------------------------------
# 6. 선형결합 평면 그리기
#    p = c*a1 + d*a2
# -------------------------------------------------
c = np.linspace(-1.5, 2.5, 15)
d = np.linspace(-1.5, 2.5, 15)

C, D = np.meshgrid(c, d)

X = C * a1[0] + D * a2[0]
Y = C * a1[1] + D * a2[1]
Z = C * a1[2] + D * a2[2]

ax.plot_surface(
    X, Y, Z,
    color="cyan",
    alpha=0.18,
    edgecolor="gray",
    linewidth=0.3
)

# -------------------------------------------------
# 7. 영벡터 표시
# -------------------------------------------------
ax.scatter(
    zero[0], zero[1], zero[2],
    color="black",
    s=70,
    label=r"$0=(0,0,0)$"
)

ax.text(
    0, 0, 0,
    "  0 = (0, 0, 0)",
    color="black",
    fontsize=10
)

# -------------------------------------------------
# 8. 그래프 꾸미기
# -------------------------------------------------
ax.set_title(
    r"Linear combinations of $a_1$, $a_2$"
    "\n"
    r"Plane: $2x-3y+5z=0$",
    fontsize=15
)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_xlim(-5, 8)
ax.set_ylim(-8, 18)
ax.set_zlim(-4, 10)

ax.view_init(elev=24, azim=-55)
ax.grid(True)

plt.tight_layout()
plt.show()
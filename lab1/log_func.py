def activation(S):
    if S < 0.5:
        return 0
    else:
        return 1

data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]


for x1, x2, x3 in data:

    print("x1 =", x1, "; x2 =", x2, "; x3 =", x3)

    S1 = -x1 - x3 + 1
    Y1 = activation(S1)
    print("S1 = -x1 - x3 + 1 =", S1)

    if S1 < 0.5:
        print("Y1 = 0 (S < 0.5)")
    else:
        print("Y1 = 1 (S >= 0.5)")

    S2 = x1 + x2 + x3 - 2.5
    Y2 = activation(S2)
    print("S2 = x1 + x2 + x3 - 2.5 =", S2)

    if S2 < 0.5:
        print("Y2 = 0 (S < 0.5)")
    else:
        print("Y2 = 1 (S >= 0.5)")

    S3 = Y1 + Y2
    Y3 = activation(S3)
    print("S3 =", Y1, "+", Y2, "=", S3)

    if S3 < 0.5:
        print("Y = 0 (S < 0.5)")
    else:
        print("Y = 1 (S >= 0.5)")

    print()
def activation(S):
    if S < 0.5:
        return 0
    else:
        return 1


for x1 in [0, 1]:
    for x2 in [0, 1]:

        print("x1 =", x1, "; x2 =", x2)

        S1 = x1 + x2 - 1
        Y1 = activation(S1)
        print("S1 =", x1, "+", x2, "+ (-1) =", S1)

        if S1 < 0.5:
            print("Y1 = F(S) = 0 (S < 0.5)")
        else:
            print("Y1 = F(S) = 1 (S ≥ 0.5)")

        S2 = -x1 + x2 + 1
        Y2 = activation(S2)
        print("S2 =", x1, "*(-1) +", x2, "+ 1 =", S2)

        if S2 < 0.5:
            print("Y2 = F(S) = 0 (S < 0.5)")
        else:
            print("Y2 = F(S) = 1 (S ≥ 0.5)")

        S3 = Y1 + Y2
        Y3 = activation(S3)
        print("S3 =", Y1, "+", Y2, "=", S3)

        if S3 < 0.5:
            print("Y3 = F(S) = 0 (S < 0.5)")
        else:
            print("Y3 = F(S) = 1 (S ≥ 0.5)")

        print()
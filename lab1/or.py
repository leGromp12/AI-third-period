def activation(S):
    if S < 0.5:
        return 0
    else:
        return 1


w1 = 1
w2 = 1

for x1 in [0, 1]:
    for x2 in [0, 1]:

        S = x1 * w1 + x2 * w2
        Y = activation(S)

        print("x1 =", x1, "; x2 =", x2)
        print("S =", x1, "*", w1, "+", x2, "*", w2, "=", S)

        if S < 0.5:
            print("Y = F(S) = 0 (оскільки S < 0.5)")
        else:
            print("Y = F(S) = 1 (оскільки S > 0.5)")

        print()
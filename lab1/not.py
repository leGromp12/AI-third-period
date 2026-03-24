def activation(S):
    if S < -1:
        return 0
    else:
        return 1


w = -1.5

for x in [0, 1]:

    S = x * w
    Y = activation(S)

    print("x =", x)
    print("S =", x, "* (", w, ") =", S)

    if S < -1:
        print("Y = F(S) = 0 (S < -1)")
    else:
        print("Y = F(S) = 1 (S ≥ -1)")

    print()
import math
import sys

sys.stdout.reconfigure(encoding="utf-8")

def activation(S):
    return 1 / (1 + math.exp(-S))

x = [1.8, 4.5, 1.9, 5.6, 1.2, 5.5, 1.1, 5.2, 1.6, 4.3, 0.0, 5.3, 0.0, 4.6, 0.6]

w1 = 1
w2 = 1
w3 = 1

N = len(x) - 3  

E_prev = 0
epsilon = 0.0001
max_iter = 10000

iteration = 0

while True:
    E = 0

    dw1_sum = 0
    dw2_sum = 0
    dw3_sum = 0

    for i in range(N):
        x1 = x[i]
        x2 = x[i+1]
        x3 = x[i+2]
        y_true = x[i+3]

        S = w1*x1 + w2*x2 + w3*x3
        Y = activation(S)

        E += (Y - y_true)**2

        d = (Y - y_true) * (math.exp(-S) / (1 + math.exp(-S))**2)

        dw1_sum += d * x1
        dw2_sum += d * x2
        dw3_sum += d * x3

    dw1 = dw1_sum / N
    dw2 = dw2_sum / N
    dw3 = dw3_sum / N

    w1 += dw1
    w2 += dw2
    w3 += dw3

    iteration += 1

    if abs(E - E_prev) <= epsilon or iteration > max_iter:
        break

    E_prev = E


print("Number of iterations:", iteration)
print("w1 =", w1)
print("w2 =", w2)
print("w3 =", w3)
print("Error E =", E)

print("\nTesting:")

for i in range(len(x)-3):
    x1 = x[i]
    x2 = x[i+1]
    x3 = x[i+2]

    S = w1*x1 + w2*x2 + w3*x3
    Y = activation(S)

    print("Input:", x1, x2, x3, "Prediction:", Y)
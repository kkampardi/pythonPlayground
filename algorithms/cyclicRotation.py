import collections

def cyclicRotation(A, K):
    if len(A) == 0:
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]

A = [3, 8, 9, 7, 6]
K = 1

print(cyclicRotation(A, K))

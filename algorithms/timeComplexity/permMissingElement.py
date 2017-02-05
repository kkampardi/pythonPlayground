def solution(A):
    length = len(A)
    xor_sum = 0

    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index + 1)

    return xor_sum^(length + 1)



def solution(A):
    A = sorted(A)

    a = b = c = 0
    for i in reversed(A):
        a, b, c = i, a, b
        if a + b > c and a + c > b and c + b > a:
            return 1
    else:
        return 0



######## OR ##########

def solution(A):
    return len(set(A))




######## OR ##########

def solution(A):
    A = sorted(A)
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

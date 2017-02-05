def solution(N, A):
    result = [0]*N

    for command in A:
        if 1 <= command <= N:
            result[command-1] += 1
        else:
            result[:] = [max(result)]*N

    return result

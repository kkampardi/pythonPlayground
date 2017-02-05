def solution(A):
    counter = [0]*len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else:
            if counter[element-1] != 0:
                return 0
            else:
                counter[element-1] = 1

    return 1

olution(A):
    if len(A) == 0:
        distinct = 0
    else:
        distinct = 1

        A.sort()
        for index in xrange(1, len(A)):
            if A[index] == A[index-1]:
                # The same element as the previous one
                continue
            else:
                # A new element
                distinct += 1

    return distinct

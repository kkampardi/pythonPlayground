olution(A):
    A_len = len(A)
    if A_len < 3:
        # N is an integer within the range [0..1,000,000]
        # if the list is too short, it is impossible to
        # find out a triangular.
        return 0

    A.sort()

    for index in xrange(0, A_len-2):
        if A[index]+A[index+1] > A[index+2]:
            return 1
        # The list is sorted, so A[index+i] >= A[index+2]
        # where i>2. If A[index]+A[index+1] <= A[index+2],
        # then A[index]+A[index+1] <= A[index+i], where
        # i>=2. So there is no element in A[index+2:] that
        # could be combined with A[index] and A[index+1]
        # to be a triangular.

    # No triangular is found
    return 0

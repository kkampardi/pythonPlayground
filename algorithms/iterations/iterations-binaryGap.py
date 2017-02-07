def solution(N):
    max_gap = 0
    gap = 0

    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        # Floor division : the division of operands where the result is the quotient
        # in witch the digits after the decima point are removed. But if one of the
        # operands is negative the result is floored, i.e rounded away from zero
        # e.g. 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
        N //= 2

    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                gap = 0
        N //= 2

    return max_gap


print (solution(9))

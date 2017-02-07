"""
def getTheGaps(N):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)

    while N > 0 and N%2 == 0:
        N //= 2
        print("Skipping: " + str(N) )

    while N > 0:
        # print ("N before div: " + str(N))
        remainder = N%2
        print( "remainder:  " + str(remainder))
        if remainder == 0:
            # Inside a gap
            current_gap += 1
            print ("inside the gap: " + str(current_gap))
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2
        print ("N after div: " + str(N))

    return max_gap

n = 9

gaps =  getTheGaps(n)

print (gaps)
"""

def solution(N):
    remainder = 0
    gap = 0
    max_gap = 0

    if N == 0: return [0]

    while N > 0 and N%2 == 0:
        """
        It performs floor division on operators and assign value to the left operand
        c //= a is equivalent to c = c // a
        """
        N //= 2

    print N

    while N > 0:
        remainder = N%2
        print remainder
        if remainder == 0:
            gap += 1
        # gap ends
        else:
            if gap != 0:
                max_gap = max(gap, max_gap)
                gap = 0
        """
        The left operands value is
        moved right by the number of bits specified by the right operand.
        a >> = 15 (means 0000 1111)
        """
        N >>= 1

    return max_gap

result = solution(9.001)
print result

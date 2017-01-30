
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
        #print ("N after div: " + str(N))

    return max_gap

n = 9

gaps =  getTheGaps(n)

print (gaps)

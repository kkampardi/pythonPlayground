
def solution(N):

    # first remove spaces aNd dashes
    N = N.replace(" ", "")
    N = N.replace("-", "")
    reformated = ""

    print reformated
    # then add the apropriate dashes
    for i in xrange(0,len(N), 3):
        start = i
        end = i+3
        reformated += N[start:end] + '-'

    reformated = reformated[:-1]
    print str( reformated )

solution("778   --- 778-778-778-778")

##: Multiply two numbers together
##: Multiply by 2, devide by 2 and add mynbers

##: AKA = Mediation and Duplication method

import time

CHACHE = {}


def russian(a, b):

    x = a; y = b
    z = 0
    while x > 0:
        if x%2 == 1: z = z+y
        y = y << 1      # same as y /= 2 or y = y /2
        x = x >> 1
        print('{} {}'.format(x, y))
    return z

def russian_optimized(a, b):
    key = (a,b)
    if key in CHACHE:
        z = CHACHE[key]

    else:
        x = a; y = b
        z = 0
        while x > 0:
            if x%2 == 1: z = z+y
            y = y << 1      # same as y /= 2 or y = y /2
            x = x >> 1
            print('{} {}'.format(x, y))
        CHACHE[key] = z
    return z

''' Test russian function '''
def test_russian():
    ''' testing algorithms efficiency '''
    assert  russian(357, 16) == 5712

    start_time = time.time()
    print(russian(357, 16))
    print('Russian algorithm took %f seconds' % (time.time()- start_time))


def test_russian_optimized():
    ''' testing algorithms efficiency '''
    assert russian_optimized(357, 16) == 5712

    start_time = time.time()
    print(russian_optimized(357, 16))
    print('Russian optimized algorithm took %f seconds' % (time.time() - start_time))



test_russian()
test_russian_optimized()
def solution(N):
    i = 1

    if N > 0:
        for i in range(1,N):
            if i%3 == 0 and i%5 == 0  and i%7 == 0:
                i = "FizzBuzzWoof"
                print i
            elif i%3 == 0 and i%5 == 0:
                i = "FizzBuzz"
                print i
            elif i%3 == 0 and i%7 == 0:
                i = "FizzWoof"
                print i
            elif i%3 == 0:
                i = "Fizz"
                print i
            elif i%5 == 0:
                i = "Buzz"
                print i
            elif i%7 == 0:
                i  = "Woof"
                print i
            else:
                print(i)


solution(25)

n = 1
while (n==1):
    for num in range(2,51,2):

        if (num % 5 == 0) and (num % 3 == 0):
            print("foobar")
        elif (num % 3 == 0):
            print("foo")
        elif (num % 5 == 0):
            print("bar")
        else:
            print(num)
            n += 1



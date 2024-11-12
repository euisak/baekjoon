while True:
    try:
        a = input()
        if int(a) == 0:
            break
        b = 0
        for i in range(len(a)):
            if a[i] == a[-(i)-1]:
                b = b
            else:
                b += 1
        if b == 0:
            print("yes")
        else:
            print("no")
                

    except:
        break
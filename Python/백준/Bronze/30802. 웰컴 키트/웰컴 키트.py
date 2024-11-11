while True:
    try:
        t = int(input())
        l = []
        a = 0
        f = 0
        l.extend(list(map(int, input().split())))
        b,c = map(int, input().split())
        if len(l) != 6:
            break
        if sum(l) != t:
            break

        for i in range(len(l)):
            f = l[i] // b
            a += f
            if l[i] % b != 0:
                a += 1
            else:
                continue
        print(a)
        print(t//c, t%c)

    except:
        break
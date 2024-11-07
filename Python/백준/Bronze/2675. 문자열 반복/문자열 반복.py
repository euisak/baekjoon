a=int(input())

for i in range(a):
    b, c = input().split()
    for x in range(len(c)):
        print(c[x]*int(b), end='')
    print()


#---------------------

a= int(input())
b= []

for i in range(a):
    c, d = input().split()
    b.append(d)
    c= int(c)

for y in range(a): 
    for f in range(len(b[y])):
        for p in range(c):
            print(b[y][f], end="")
    print()

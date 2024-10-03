a,b,c,d,e= map(int,input().split())
output= (a**2+b**2+c**2+d**2+e**2)%10
print(output)

b=0
items = list(map(int, input().split()))
for item in items:
    b += item**2
print(b%10)

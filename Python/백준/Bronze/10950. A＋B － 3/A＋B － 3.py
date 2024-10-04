a=int(input())
output= ""
for i in range(a):
    b,c = map(int, input().split())
    output += str(b+c) + "\n"
print(output)
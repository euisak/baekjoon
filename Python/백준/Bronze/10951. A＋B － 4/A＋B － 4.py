while True:
    try:
        a, b= map(int, input().split())
        print(a + b)
    except:     # 오류 발생할 경우 except 실행
        break


''' 
while True:
    a, b= map(int, input().split())   이 경우 맞지 않는 형식 입력 시 오류 발생
    print(a + b)  
        '''

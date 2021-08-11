num = int(input("숫자를 입력하세요: "))# 1: 입력받은 자료형이 숫자임을 확인
isSosu = True
for i in range(2, num//2): # 2: 입력받은 숫자까지 반복하기
    if num % i == 0: # 3: 조건문작성
        print(i) # 4: 조건문 내에서 출력하기
        isSosu = False
        break
    
if isSosu == True:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
        



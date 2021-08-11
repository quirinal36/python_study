def total(a, b):
    c = a + b
    return c

def avg(sub1, sub2, sub3):
    total = (sub1 + sub2 + sub3) / 3
    return total
"""
answer = total(1, 2)
print("합계는 {}입니다.".format(answer))

answer = total(3, 5)
print("합계는 {}입니다.".format(answer))
"""
sco1 = int(input("첫 번째 과목의 점수를 입력해주세요 : "))
sco2 = int(input("두 번째 과목의 점수를 입력해주세요 : "))
sco3 = int(input("세 번째 과목의 점수를 입력해주세요 : "))
score = avg(sco1, sco2, sco3)
print("평균은 {}입니다.".format(score))
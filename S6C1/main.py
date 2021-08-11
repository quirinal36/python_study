import fn
import random as rand

# 임의의 숫자 10개를 저장하는 리스트를 만든다. (범위 1~100)
li = [0] * 10
for i in range(10):
    li[i] = rand.randint(1, 100)
print(li)

# 1. 합계 구하기
result = fn.sum_li(li)
print("리스트의 모든 값의 합계:{}".format(result))
# 2. 짝수의 개수 구하기
print("짝수의 개수:{}".format(fn.even(li)))
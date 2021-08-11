# 1. 리스트의 원소들의 모든 합계를 계산하는 함수
def sum_li(arr):
    total = 0

    for n in arr:
        total = total + n

    return total

# 2. 리스트의 원소들 중 짝수의 개수를 세는 함수
def even(arr):
    cnt = 0
    for n in arr:
        if n % 2 == 0:
            cnt+=1
    return cnt

# 3. 짝수값의 합계
def even_sum(arr):
    total = 0
    pass
    return total
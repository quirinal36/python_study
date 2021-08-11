def solution(s, n):
    result = ""
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    for c in s:
        if c == " ":
            result = result + c
        elif c.isupper():
            idx = capital.index(c)
            change = idx + n
            if change > 25:
                change = change%25 - 1
            result = result + capital[change]
        elif c.islower():
            idx = small.index(c)
            change = idx + n
            if change > 25:
                change = change%25 - 1
            result = result + small[change]
    return result

p = input("문장을 입력하세요: ")
num = int(input("숫자를 입력하세요: "))
res = solution(p, num)
print(res)

s="AbCd"
if s[0].isupper() == True:
   print("{}는 대문자입니다.".format(s[0]))

if s[1].islower() == True:
    print("{}는 소문자입니다.".format(s[1]))

for c in s:
    print(c)

idx = s.index("C")
print("{}는 문장의{}번째에 위치합니다.".format("C", idx))

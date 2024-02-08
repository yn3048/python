# 문자열 자료형
# 문자열이란? 문자, 단어 등으로 구성된 문자들의 집합
a = "Life is too short,\n You need python"
# print(a)
b = """Life is too short, 
        You need python"""
# print(b)

# 문자열 더하기
a = "Python"
b = " is fun"
# print(a + b)
# # 문자열 곱하기
# print(a * 3)

# print("=" * 50)
# print("정보처리기사!")
# print("=" * 50)

# 문자열 길이 구하기
# len 함수 , 공백도 길이에 포함
a = "Life is too short"
# print(len(a))

# 문자열 인덱싱(가리킨다), 슬라이싱(잘라낸다)
a = "Life is too short"
# print(a[0])
# print(a[1])
# print(a[-1]) # 젤뒷자리
# print(a[-2])

b = a[0] + a[1] + a[2] + a[3]
# print(b)
a = "Life is too short"
# print(a[0:4])
# 슬라이싱 [시작_번호:끝_번호]
# 0 <= a < 4
a = "Life is too short"
# print(a[:]) # 전체 출력
# print(a[:6])
# print(a[12:])

# 슬라이싱으로 문자열 나누기
a = "20240131Rainy"
date = a[:8]     #처음부터 7번째까지
weather = a[8:]  #8번째부터 끝까지
# print(date)
# print(weather)

# a = "pithon"
# print(a[1])
# a[1] = 'y'  #오류남

# 문자열 포매팅
# 현재 온도는 18도 입니다.
# 1. 숫자 바로 대입
print("현재 온도는 %d 도 입니다." % 18)
# 2. 문자열 바로 대입
print("현재 온도는 %s 도 입니다." % "five")
# 숫자를 넣기 위해서는 %d, 문자는 %s









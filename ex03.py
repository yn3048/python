# 자료형 리스트
# 대괄호 ([]), 각 요소값들은 쉼표(,)로 구분
add = [1, 3, 5, 7, 9]
# print(add)
# 리스트는 여러가지 생김새
a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life']
e = [1, 2, ['a', 'b']]
# print(c[2])
# print(e[2])
# print(e[2][1])

# 리스트의 수정과 삭제
# 리스트의 값 수정하기
a = [1, 2, 3]
# print(a)
# a[2] = 4
# print(a)

#del 함수를 사용해 리스트 요소 삭제
# a = [1, 2, 3]
# print(a)
# del a[1] 
# print(a)

# # 슬라이싱으로 여러개 삭제
# a = [1,2,3,4,5]
# print(a)
# del a[2:]  #index 2부터 끝까지 삭제
# print(a)


# 리스트 관련 함수
# # append 요소 추가하기
# a = [1,2,3]
# a.append(4)
# print(a)
# a.append([5, 6])
# print(a)
# 리스트 안에는 어떤 자료형도 추가할 수 있다

# index 인덱스 번호 반환
a = [1,2,3]
# print(a.index(3))
# print(a.index(1))
# print(a.index(0))

# insert 리스트에 요소 삽입 insert(a, b)
# a번째 위치에 b를 삽입하는 함수
# a = [1,2,3]
# a.insert(0, 4)
# print(a)

# remove 리스트 요소 제거, 첫번째 나오는 값을 제거
# a = [1,2,3,1,2,3]
# a.remove(3)
# print(a)
# a.remove(3)
# print(a)

# pop 리스트 요소 끄집어 내기
a = [1,2,3]
print(a.pop(1))    # 인덱스 위치 1번이 나감, ()가 공백일 경우 마지막 숫자가 나감
print(a)



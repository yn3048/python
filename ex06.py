# 집합 자료형 set
s1 = set([1,2,3])
print(s1)

# 집합 자료형은 중복을 허용하지 않는다
# 문자열은 순서가 없다
s2 = set("pythono")
print(s2)

# 교집합 & intersection()
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])
print(s1 & s2)
print(s1.intersection(s2))
# 합집합 | , 함수 union()
print(s1 | s2)
print(s1.union(s2))

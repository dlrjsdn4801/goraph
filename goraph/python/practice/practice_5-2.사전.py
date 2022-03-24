# 사전은 중복허용 X
cabinet = {3:"이건우", 20:"홍길동"}

print(cabinet[3])
print(cabinet.get(3))

print(cabinet.get(100)) # None
print(cabinet.get(100, "사용가능")) # 없으면 사용가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"4번":"강호동"} # str 가능
print(cabinet["4번"])

# new? 추가
print(cabinet)
cabinet["6번"] = "신금희"
print(cabinet)

# 삭제
del cabinet["6번"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 클리어
#cabinet.clear()
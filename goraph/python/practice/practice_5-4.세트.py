# 집합 (set)
# 중복 , 순서 X

my_set = {1,3,4,4,4,2}
print(my_set)

R = {"이건우", "홍길동", "김지우"}
python = set(["김지우", "제갈량"])

# 교집합
print(R & python)
print(R.intersection(python))

# 합집합
print(R | python)
print(R.union(python))

# 차집합
print(R - python)
print(R.difference(python))

# 추가
python.add("좋은밤")

# 삭제
python.remove("제갈량")
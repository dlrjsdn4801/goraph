# 지하철 칸별로 10명, 20명, 나

subway1 = 10
subway2 = 20
subway3 = "이건우"

subway = [subway1,subway2,subway3]

subway4 = [ "이", "건", "우" ]

#건은 몇 번째 칸?
print(subway4.index("건"))

# "다" 추가
subway4.append("다")

# 이 을 우 , 다 사이에?
subway4.insert(3, "이")

# 뒤에서부터 한 명씩 꺼낸다
print(subway4.pop())

# 같은 이름 몇 개?
print(subway4.count("이"))

# 정렬
num_list = [3,1,6,4,2]
num_list.sort()

# 반대로 정렬
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양 자료형 함께
num_list = [6,4,3,2,1]
name_list = ("이건우","홍길동,",30,True)
num_list.extend(name_list)
print(num_list)

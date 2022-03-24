#랜덤함수, 기본적으론 최솟값(1) 포함인듯??
from random import *
print(random()) # 0.0 ~ 1.0 미만 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만 값 생성
print(int(random() * 10)) # 0 ~ 10 미만 값 (정수) 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 값 (정수) 생성

print(int(random() * 10) + 1) # 1 ~ 10 이하 값 (정수) 생성
print(randrange(1, 11)) # 1 ~ 11 미만 값 (정수) 생성
print(randint(1, 10)) # 1 ~ 10 이하 값 (정수) 생성

오프라인 = randint(4, 28)
print("오프라인 약속 날짜는", 오프라인, "입니다.")
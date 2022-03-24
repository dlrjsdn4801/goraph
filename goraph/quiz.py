lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lst)

from random import *

shuffle(lst)
print(lst)

chk = sample(lst,1)
cof = sample(lst,3)

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : ", chk)
print(" 커피 당첨자 : ", cof)
print(" -- 축하합니다 -- ")

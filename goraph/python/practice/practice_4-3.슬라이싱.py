#슬라이싱
joomin = "030110-1234567" # 셀 때에는 맨 앞이 0

print("내 성별은 : ", joomin[7])
print("내 생년은 : ", joomin[0:2]) # 0번째부터 2번째 전까지
print("내 생월은 : ", joomin[2:4])
print("내 생일은 : ", joomin[4:6])

print("내 생년월일은 : ", joomin[0:6])
print("내 생년월일은 : ", joomin[:6]) # 처음 값 생략
print("내 뒷자리는 : ", joomin[7:]) # 뒷 값 생략
print("내 뒷자리(뒤에서부터)는 : ", joomin[-7:]) # 뒤에서부터 n번째까지
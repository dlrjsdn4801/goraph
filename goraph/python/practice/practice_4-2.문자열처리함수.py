문자열 = "Python is Amazing"

print(문자열.lower())
print(문자열.upper())
print(문자열[0].isupper()) # 0번쨰문자가 대문자?
print(len(문자열)) # 문자열길이
print(문자열.replace("Python", "R"))

index = 문자열.index("n") #n 위치
print(index)
index = 문자열.index("n", index + 1) #처음 n 위치 + 1 부터의 n 위치
print(index)

print(문자열.find("Python")) #"-"위치
print(문자열.find("R")) #없을 때에는 -1 출력
#print(문자열.index("R")) #없을 때에는 오류

print(문자열.count("n")) # n이 몇 번
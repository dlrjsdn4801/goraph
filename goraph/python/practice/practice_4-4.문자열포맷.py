print("a" + "b") # ab
print("a", "b") # a b

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아합니다." % "냠냠")

print("나는 %s살입니다." % 20)

print("나는 %s과 %s을 좋아합니다." % ("녹색","흰색"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}살, {}사는 {}입니다.".format(20,"충북학사","이건우"))
print("나는 {0}살, {1}사는 {2}입니다.".format(20,"충북학사","이건우"))
print("나는 {2}살, {0}사는 {1}입니다.".format(20,"충북학사","이건우"))

 # 방법 3 print("나는 ","살, ","사는 ","입니다." sep(20))
print("나는 {age}살, {where}사는 {name}입니다.".format( age = 20, where = "충북학사", name = "이건우" ))
print("나는 {age}살, {where}사는 {name}입니다.".format(  where = "충북학사", age = 20, name = "이건우" ))

# 방법 4
age = 20
name = "이건우"
print(f"나는 {age}살이며, {name}라고 합니다.")
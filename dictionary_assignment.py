# 가이드라인 2
youngbeen = {
    "name" : "youngbeen",
    "age" : 22,
    "birth" : "2001년 12월 22일",
    "sex" : "female",
    "phone" : "010-3420-5470"
}

haesoo = {
    "name" : "haesoo",
    "age" : 40,
    "birth" : "1981년 11월 21일",
    "sex" : "male",
    "phone" : "모름"
}

kyoohyung = {
    "name" : "kyoohyung",
    "age" : 38,
    "birth" : "1983년 11월 29일",
    "sex" : "male",
    "phone" : "모름"
}

# 가이드라인 3
Name = [1,2,3]
Age = [1,2,3]
Birth = [1,2,3]
Sex = [1,2,3]
Phone = [1,2,3]

# 가이드라인 4
Name[0] = youngbeen["name"]
Name[1] = haesoo["name"]
Name[2] = kyoohyung["name"]

Age[0] = youngbeen["age"]
Age[1] = haesoo["age"]
Age[2] = kyoohyung["age"]

Birth[0] = youngbeen["birth"]
Birth[1] = haesoo["birth"]
Birth[2] = kyoohyung["birth"]

Sex[0] = youngbeen["sex"]
Sex[1] = haesoo["sex"]
Sex[2] = kyoohyung["sex"]

Phone[0] = youngbeen["phone"]
Phone[1] = haesoo["phone"]
Phone[2] = kyoohyung["phone"]

print("이름 리스트는", Name)
print("나이 리스트는", Age)
print("생일 리스트는", Birth)
print("성별 리스트는", Sex)
print("전화번호 리스트는", Phone)
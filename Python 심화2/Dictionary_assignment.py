Dic = {}

while True:
        key = int(input("키를 입력해주세요: "))
        value = input("value를 입력해주세요: ")
        if ((key == 0) and (value == "0")):
            print("그만")
            print(Dic)
            break
        Dic[key] = value


key_list = list(Dic.keys())
value_list = list(Dic.values())
item_list = list(Dic.items())
print(key_list)
print(value_list)
print(item_list)


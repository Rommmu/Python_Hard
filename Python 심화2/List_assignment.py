List = []

for x in range(0, 15):
    number = int(input("숫자를 입력하세요 : "))
    List.append(number)
    if(x == 14):
        print(List)

for x in List:
    if (x % 2 == 0):
        List.remove(x)
print(List)

for x in List:
    if (x % 3 == 0):
        List.remove(x)
print(List)

print(List.pop(0))
List.insert(1, 2)
List.insert(2, 3)
print(List)
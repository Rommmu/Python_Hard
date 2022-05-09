# 여러 형태 리스트 출력해보기
list1 = []
list2 = [1, 2, 3]
list3 = ["one", "two", "three"]
list4 = [1, "two", 3]
list5 = [1, 2, ["three", "four"]]

print("list1 : ", list1)
print("list2 : ", list2)
print("list3 : ", list3)
print("list4 : ", list4)
print("list5 : ", list5)

# 리스트 인덱싱 해보기
print(list5[0], list5[1], list5[2])

# 리스트 슬라이싱 해보기
print(list5[0:2])

# 리스트 덧셈
list6 = list2 + list3
print("list6 : ", list6)

# 리스트 반복
list7 = list2 * 3
print("list7 : ", list7)

# 리스트 수정
list4[1] = 2
print("list4 : ", list4)

# 리스트 삭제
del list5[2]
print("list5 : ", list5)

#슬라이싱을 통한 수정과 삭제
list8 = ["one", "two", "three", 4, 5]

list8[0:3] = [1,2,3]
print("list8 : ", list8)

del list8[3:]
print("list8 : ", list8)
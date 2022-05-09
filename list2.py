List = [1, 2, "a", "b", "c"]
# 리스트 수정 -- 인덱싱을 사용해서 "c"를 5로 수정하고 print()문을 사용해 출력해주세요
List[4] = 5
print(List)

# 리스트 수정 -- 슬라이싱을 사용해서 "a"와 "b" 를 3과 4로 수정하고 print()문을 사용해 출력해주세요
List[2:4] = [3,4]
print(List)

# 리스트 삭제 -- 인덱싱을 사용해서 5를 삭제하고 print()문을 사용해 출력해주세요
del List[4]
print(List)

# 리스트 삭제 -- 슬라이싱을 사용해서 3과 4를 삭제하고 print()문을 사용해 출력해주세요
del List[2:4]
print(List)
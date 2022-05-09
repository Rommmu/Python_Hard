Dic = {1 : 'a', 2 : 'b'}
# 딕셔너리 쌍 추가 후 print()문을 사용해 출력해주세요 -- Key가 숫자일 때
Dic[3] = 'c'
print(Dic)
# 딕셔너리 쌍 추가 후 print()문을 사용해 출력해주세요 -- Key가 문자열일 때
Dic['four'] = 'd'
print(Dic)
# 딕셔너리 쌍 추가 후 print()문을 사용해 출력해주세요  -- Value가 숫자일 때
Dic[5] = '5'
print(Dic)

# 딕셔너리 쌍 추가 후 print()문을 사용해 출력해주세요  -- Value가 문자일 때
Dic[6] = 'f'
print(Dic)

# 딕셔너리 쌍 추가 후 print()문을 사용해 출력해주세요  -- Value가 리스트일 때
Dic['seven'] = ['g', 'h', 'i']
print(Dic)


# 딕셔너리 쌍 삭제하기
del Dic[6]
print(Dic)


# 딕셔너리 쌍 수정하기
Dic[5] = 'e'
print(Dic)


# Key를 사용해 Value 얻기 -- 모든 요소 값을 print()문을 사용해 출력해주세요 
print(Dic[1], Dic[2], Dic[3], Dic['four'], Dic[5], Dic['seven'])
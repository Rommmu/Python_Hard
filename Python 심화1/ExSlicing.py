sentence = "we are skhu likelion"
# 인덱싱을 이용해 문자 are 뽑아내기
word1 = sentence[3] + sentence[4] + sentence[5]
print("word1은 " + word1)


# 슬라이싱을 이용해 문자 are 뽑아내기
word2 = sentence[3:6]
print("word2는 " + word2)

# 슬라이싱 범위 알아보기 -- skhu 문자 뽑기
word3 = sentence[7:10]
word4 = sentence[7:11]
print("word3는 " + word3)
print("word4는 " + word4)


# 시작 번호 생략해서 we are 뽑아내기
word5 = sentence[:6]
print("word5는 " + word5)


# 끝 번호 생략해서 skhu likelion 뽑아내기
word6 = sentence[7:]
print("word6은 " + word6)


# 시작번호 끝 번호 생략해서 둘 다 뽑아내기
word8 = sentence[:]
print("word8는 " + word8)


# - 숫자를 통해 likelion 슬라이싱하기
word9 = sentence[-8:]
print("word9는 " + word9)

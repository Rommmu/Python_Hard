# 가이드라인 2 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# 가이드라인 3
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '-']

# 가이드라인 4
sentence1 = # 요소 가이드라인 5처럼 더하기 죄송해요 너무 노가다라 저는 안하고 싶어요
# we are skhu likelion
sentence2 = # 요소 가이드라인 5처럼 더하기 죄송해요 너무 노가다라 저는 안하고 싶어요
# hack your life
sentence3 = # 요소 가이드라인 5처럼 더하기 죄송해요 너무 노가다라 저는 안하고 싶어요
# my name is youngbeen

print(sentence1) # -> 출력 : we are skhu likelion
print(sentence2) # -> 출력 : hack your life
print(sentence3) # -> 출력 : my name is youngbeen

# 가이드라인 5
birth = number[1] + number[-2] + number[-2] + number[0] + number[0] + number[1] + number[1] + number[1]
phone = str(number[-2]) + str(number[0]) + str(number[-2]) + number[-1]+ str(number[2]) + str(number[3]) + str(number[1]) + str(number[-2]) + number[-1] + str(number[4]) + str(number[3]) + str(number[6]) + str(number[-2])
school = number[1] + number[-2] + number[1] + number[0] + number[0] + number[3] + number[-2] + number[3] + number[0]

print("제 생일은 %d 입니다." % birth)
print("제 전화번호는 %s 입니다." % phone)
print("제 학번은 %d 입니다." % school)
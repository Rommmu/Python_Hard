# 가이드라인 2 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 가이드라인 3
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '-']

# 가이드라인 4
sentence1 = alphabet[7:9]
# hi
sentence2 = alphabet[-2] + alphabet[-12] + alphabet[-6] + alphabet[-13] + alphabet[6] + alphabet[1] + alphabet[4] + alphabet[4] + alphabet[-13]
# youngbeen
sentence3 = alphabet[2] + alphabet[-12] + alphabet[3] + alphabet[4]
# code

print(sentence1)
print(sentence2)
print(sentence3)

# 가이드라인 5
birth = number[1] + number[-2] + number[-2] + number[0] + number[0] + number[1] + number[1] + number[1]
phone = str(number[-2]) + str(number[0]) + str(number[-2]) + number[-1]+ str(number[2]) + str(number[3]) + str(number[1]) + str(number[-2]) + number[-1] + str(number[4]) + str(number[3]) + str(number[6]) + str(number[-2])
school = number[1] + number[-2] + number[1] + number[0] + number[0] + number[3] + number[-2] + number[3] + number[0]

print("제 생일은 %d 입니다." % birth)
print("제 전화번호는 %s 입니다." % phone)
print("제 학번은 %d 입니다." % school)
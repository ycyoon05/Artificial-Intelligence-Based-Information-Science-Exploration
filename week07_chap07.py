trolly = ['김광석CD', '아이폰15프로']
print(trolly)

foods = ['다시마', '멸치']
trolly.append(foods)
print(trolly)
print(trolly[2][1])
# print(trolly.pop()) # 리스트의 맨 마지막 원소(['다시마', '멸치'])를 리턴 후 삭제
# print(trolly[2].pop()) # 멸치 원소를 리턴 후 삭제
print(trolly[2].pop(0)) # 다시마 원소를 리턴 후 삭제
print(trolly)

trolly[2].append('다시마')
print(trolly)

trolly[2].insert(0, '딸기')
print(trolly)

# trolly.pop(1)
# trolly.insert(1, '아이폰15')
# print(trolly)

# trolly[1:2] = '아이폰15' # ['김광석CD', '아', '이', '폰', '1', '5', ['딸기', '멸치', '다시마']]
trolly[1:2] = ['아이폰15']
print(trolly)
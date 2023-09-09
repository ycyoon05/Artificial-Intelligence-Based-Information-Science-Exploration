student_id = 20115
student_name = "윤영찬"
subject = ["파이썬", "통계학", "수학"]
score = 3.7

print(f"학번이 {student_id}인 {student_name} 학생은 {subject}을(를) 수강하였고, 학점이 {score}입니다.")

print(type(student_id), type(student_name), type(subject), type(score), type(True)) # 각 변수의 자료 타입 출력
print(id(student_id), id(student_name), id(subject), id(score)) # 각 변수의 ID값 출력

if False: # boolean type
    print("무조건 출력 안됩니다.")
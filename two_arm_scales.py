import random
count = 3
answer = random.choice(range(1,13))
while count > 0:
	left = input("왼쪽에 올릴 추들을 입력해주세요.")
	if str(answer) not in left.split():
		left_weight = 4
	else:
		left_weight = 3.5
	right = input("오른쪽에 올릴 추들을 입력해주세요.")
	if str(answer) not in right.split():
		right_weight = 4
	else:
		right_weight = 3.5
	if left_weight > right_weight:
		print("저울이 왼쪽으로 기울었습니다.")
	elif left_weight < right_weight:
		print("저울이 오른쪽으로 기울었습니다.")
	else:
		print("저울이 평형입니다.")
	count -= 1
if int(input("다른 추들보다 가벼운 가짜 추는 몇 번인가요?")) == answer:
	print("정답입니다!")
else:
	print("오답입니다... 정답은 {}번이었습니다.".format(answer))

import random

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
answer = ['A','B','C','D','E','F','G','H'] * 2
answer = ['A','B','C','D','E','F','G','H', 'A','B','C','D','E','F','G','H']
random.shuffle(answer)
remained = len(numbers) // 2
record = 0
while remained:
	print("""
	{} {} {} {}
	{} {} {} {}
	{} {} {} {}
	{} {} {} {}
	""".format(
		numbers[0],
		numbers[1],
		numbers[2],
		numbers[3],
		numbers[4],
		numbers[5],
		numbers[6],
		numbers[7],
		numbers[8],
		numbers[9],
		numbers[10],
		numbers[11],
		numbers[12],
		numbers[13],
		numbers[14],
		numbers[15]
		)
	)
	first = input("첫 번째 숫자를 입력해주세요: ")
	second = input("두 번째 숫자를 입력해주세요: ")
	for i in range(len(numbers)):
		if type(numbers[i]) != int and numbers[i] != '.':
			numbers[i] = i + 1
	if answer[int(first) - 1] == answer[int(second) - 1]:
		numbers[int(first) - 1] = '.'
		numbers[int(second) - 1] = '.'
		remained -= 1
	else:
		numbers[int(first) - 1] = answer[int(first) - 1]
		numbers[int(second) - 1] = answer[int(second) - 1]
	record += 1
print("당신은 {}회만에 게임을 클리어하였습니다!".format(record))

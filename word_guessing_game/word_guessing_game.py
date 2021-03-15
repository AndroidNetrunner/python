import random
words = open("word_list.txt", "r", encoding="UTF-8").readlines()
fake = '\n'
while fake == '\n':
    fake = random.choice(open("word_list.txt", "r", encoding="UTF-8").read())
answers = random.sample(words, 3)
questions = [fake]
for i in range(len(answers)):
    if answers[i][-1] == '\n':
        answers[i] = answers[i][:-1] 
for i in answers:
    questions += list(i)
random.shuffle(questions)
is_correct = False
while not is_correct:
    print(" ".join(questions))
    answer = input("숨겨진 세 개의 단어를 적어주세요: ")
    if sorted(answer.split()) == sorted(answers):
        is_correct = True 
print("정답을 맞히셨습니다!")


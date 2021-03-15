def diff(sentence, typing):
    i = 0
    result = 0
    while i < len(sentence) and i < len(typing):
        if sentence[i] != typing[i]:
            result += 1
        i += 1
    if len(sentence) > len(typing):
        return result + len(sentence) - len(typing)
    if len(sentence) < len(typing):
        return result + len(typing) - len(sentence)
    return result

import datetime

song = input("""어떤 노래로 타자 연습을 진행하고 싶으신가요?
""")
lyrics = open(song, "r", encoding='UTF-8').readlines()
start = datetime.datetime.now()
wrong = 0
for sentence in lyrics:
    if sentence != "\n":
        if sentence[-1] == '\n':
            sentence = sentence[:-1]
        print(sentence)
        typing = input()
        wrong += diff(sentence, typing)
record = datetime.datetime.now() - start
print("""소요 시간: {}분 {}초
오타 개수: {}""".format(record.seconds // 60, record.seconds % 60, wrong))
print("소요 시간은" + record+ "입니다.")

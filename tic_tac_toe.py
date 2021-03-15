def game_ends(play):
    if play[0] == play[1] and play[1] == play[2]:
        return True
    elif play[3] == play[4] and play[4] == play[5]:
        return True
    elif play[6] == play[7] and play[7] == play[8]:
        return True
    elif play[0] == play[4] and play[4] == play[8]:
        return True
    elif play[2] == play[4] and play[4] == play[6]:
        return True
    elif play[0] == play[3] and play[3] == play[6]:
        return True
    elif play[1] == play[4] and play[4] == play[7]:
        return True
    elif play[2] == play[5] and play[5] == play[8]:
        return True
    else:
        return False

play = [1,2,3,4,5,6,7,8,9]
count = 0
current_turn = "A"
while not game_ends(play) and count < 9:
    print(
        """
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    """.format(play[0],play[1],play[2],play[3],play[4],play[5],play[6],play[7],play[8]))
    choice = int(input("어느 위치에 그리시겠습니까? 현재 차례: {} ".format(current_turn))) - 1
    if type(play[choice]) != str:
        play[choice] = current_turn
        current_turn = "A" if current_turn == "B" else "B"
        count += 1
    else:
        print("이미 선택된 공간입니다.")
print(
        """
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    """.format(play[0],play[1],play[2],play[3],play[4],play[5],play[6],play[7],play[8]))
if count == 9 and not game_ends(play):
    print("무승부입니다!")
else:
    print("선공이 승리하였습니다!" if current_turn == "B" else "후공이 승리하였습니다!")
# 게임 준비
#   게임판을 띄우기
print()
# 게임 진행

# 게임 종료

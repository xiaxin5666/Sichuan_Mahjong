from shuffle import shuffle
from win_judge import win_judge
from operate import get,throw,peng,gang
from win_test import test

if __name__ == "__main__":
    player_tiles_1, tiles = shuffle()
    player_tiles_1 = player_tiles_1[0]
    while True:
        g = get(player_tiles_1,tiles)
        if not g:
            break
        w = win_judge(player_tiles_1)
        if w:
            print("恭喜你，你赢了,自摸")
            print("当前牌：",player_tiles_1)
            break
        print("当前牌：",player_tiles_1)
        throw(player_tiles_1)
        test(player_tiles_1)








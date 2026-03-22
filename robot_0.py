from win_judge import win_judge
from operate import get,throw,peng,gang

#选一门牌丢弃
def throw_tile(player_tiles):
    tiao,tong,wan = 0,0,0
    for i in player_tiles:
        if i[1] == 'i':
            tiao += 1
        if i[1] == 'o':
            tong += 1
        if i[1] == 'a':
            wan += 1
    r = max(tiao, tong, wan)
    if r == tiao:
        return "tiao"
    if r == tong:
        return "tong"
    if r == wan:
        return "wan"

def play(player_tiles, tiles):
    check_tiles = False
    throw_list = []
    while True:
        get(player_tiles,tiles)
        w = win_judge(player_tiles)
        if w:
            print("机器人0赢了。")
            print("当前牌：", player_tiles)
            break
        if not check_tiles:
            check_tiles = throw_tile(player_tiles)
        #划分丢弃
        if check_tiles == "tiao":
            for i in player_tiles:
                if i[1] == 'i':
                    throw_list.append(i)
                    player_tiles.remove(i)
        if check_tiles == "tong":
            for i in player_tiles:
                if i[1] == 'o':
                    throw_list.append(i)
                    player_tiles.remove(i)
        if check_tiles == "wan":
            for i in player_tiles:
                if i[1] == 'a':
                    throw_list.append(i)
                    player_tiles.remove(i)
        if len(throw_list) > 0:
            t = throw_list.pop(0)
            print("机器人0丢弃了牌：", t)
            continue
        t = player_tiles.pop(0)
        print("机器人0丢弃了牌：", t)

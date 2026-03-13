def win_judge(player_tiles):
    if len(player_tiles) < 14:
        return False
    tiao = False
    tong = False
    wan = False
    player_tiles.sort()
    for i in range(len(player_tiles)):
        if player_tiles[i][1] == 'i':
            tiao = True
        if player_tiles[i][1] == 'o':
            tong = True
        if player_tiles[i][1] == 'a':
            wan = True
        if tiao and tong and wan:
            return False
        # 2. 遍历每一种可能的将牌，尝试移除将牌后验证剩余牌是否为4组3卡牌
    for i in range(len(player_tiles)):
        # 跳过重复的将牌判断（避免重复计算）
        if i > 0 and player_tiles[i] == player_tiles[i - 1]:
            continue
        # 找到相邻且相同的牌作为将牌
        if i + 1 < len(player_tiles) and player_tiles[i] == player_tiles[i + 1]:
            # 移除将牌，得到剩余12张牌
            remaining = player_tiles[:i] + player_tiles[i + 2:]
            if is_valid_three_card_groups(remaining):
                return True
    if player_tiles[0]==player_tiles[1] and player_tiles[2]==player_tiles[3] and\
            player_tiles[4]==player_tiles[5] and player_tiles[6]==player_tiles[7] and\
            player_tiles[8]==player_tiles[9] and player_tiles[10]==player_tiles[11] and\
            player_tiles[12]==player_tiles[13]:
        return True
    return False


def is_valid_three_card_groups(remaining):
    remaining.sort()
    i=0
    t=0
    q=0
    while len(remaining) > 0:
        if len(remaining) >= 3:
            if remaining[i] == remaining[i + 1] == remaining[i + 2]:
                remaining = remaining[:i] + remaining[i + 3:]
                if len(remaining) == 0:
                    return True
                else:
                    continue
        for j in range(len(remaining)-1):
            if (remaining[t][1] == remaining[j+1][1] and
                    int(remaining[t][-1])+1==int(remaining[j+1][-1])):
                t=j+1
                for k in range(t,len( remaining)-1):
                    if (remaining[t][1] == remaining[k+1][1] and
                        int(remaining[t][-1])+1==int(remaining[k+1][-1])):
                        remaining[t]=0
                        remaining[k+1]=0
                        remaining[0]=0
                        remaining=[x for x in remaining if x!=0]
                        t=0
                        if len(remaining) == 0:
                            return True
                        break
                break
        q+=1
        if q>=7:
            return False
    return False




if __name__ == '__main__':
    player_tiles = ['tiao1', 'tiao2', 'tiao3', 'tiao3', 'tiao3', 'tiao6', 'tiao3',
                    'tiao4', 'tiao5', 'tong2', 'tong2', 'tong2','tong3','tong3']
    print(win_judge(player_tiles))


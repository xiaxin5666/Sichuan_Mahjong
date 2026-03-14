def get(player_tiles_1,tiles):
    g = tiles.pop(0)
    player_tiles_1.append(g)
    return g

def throw(player_tiles_1):
    while True:
        try:
            g = input("请输入要丢弃的牌:")
            player_tiles_1.remove(g)
            break
        except:
            print("请输入正确的牌")

def peng(player_tiles_1,p):
    print("是否要碰？y/n")
    a = input()
    if a == "y":
        player_tiles_1.remove(p)
        player_tiles_1.remove(p)
        return p
    if a == "n":
        return False
    else:
        print("请输入正确的选项")

def gang(player_tiles_1,g):
    print("是否要杠？y/n")
    a = input()
    if a == "y":
        player_tiles_1.remove(g)
        player_tiles_1.remove(g)
        player_tiles_1.remove(g)
        return g
    if a == "n":
        return False
    else:
        print("请输入正确的选项")

if __name__ == "__main__":
    import shuffle
    player_tiles, tiles = shuffle.shuffle()
    print("摸之前",player_tiles[0],tiles)
    get(player_tiles[0],tiles)
    print("摸之后",player_tiles[0],tiles)
    throw(player_tiles[0])
    print("丢牌之后",player_tiles[0],tiles)

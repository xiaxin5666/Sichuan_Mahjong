import random
import itertools

import tile
def shuffle():
    n = 108
    tiles = []
    for i in range(4):
        tiles.append(tile.Tile.tile_list)
    tiles = list(itertools.chain(*tiles))
    #print(tiles)

    random.shuffle(tiles)
    #print(tiles)

    player_tiles = [[0 for _ in range(13)] for _ in range(4)]
    for i in range(4):
        for j in range(13):
            player_tiles[i][j] = tiles.pop(0)

    return player_tiles, tiles

if __name__ == "__main__":
    player_tiles, tiles = shuffle()
    print(player_tiles)
    print("剩余的牌数：",len(tiles))
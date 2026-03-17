import tile
import win_judge


def test(player_tiles):
    player_tiles1 = player_tiles.copy()
    for i in range(len(tile.Tile.tile_list)):
        player_tiles1.append(tile.Tile.tile_list[i])
        m = 0
        for j in range(len(player_tiles1)):
            if tile.Tile.tile_list[i] == player_tiles1[j]:
                m += 1
        if win_judge.win_judge(player_tiles1) and m<4:
            print("可以胡：",tile.Tile.tile_list[i])
        player_tiles1.remove(tile.Tile.tile_list[i])

if __name__ == "__main__":
    player_tiles = ["tiao1", "tiao2", "tiao3", "tiao3", "tiao3", "tiao3",
                    "tiao4", "tiao5", "tong2", "tong2", "tong2", "tong3", "tong3"]
    test(player_tiles)

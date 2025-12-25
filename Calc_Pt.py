import json

# ゲームのロード
def game_load(file_path):
    # ファイルのロード
    with open(file_path, 'r', encoding='utf-8') as f:
        game = json.load(f)
    return game

# 順位ポイント集計
def calc_rank_pt(placement, kills, mode):
    # 順位ポイント数
    rank_pt = 0
    normal_rank_pt = [24,18,14,10,8,6,6,4,4,4,2,2,2,2,2,0,0,0,0,0]
    wild_card_rank_pt = [10,9,8,7,6,5,4,3,2,1]

    # 通常ゲームなら
    if mode == True:
        placement_pt = normal_rank_pt[placement-1]
        kill_pt = kills
        rank_pt = placement_pt + kill_pt
    # ワイルドカードゲームなら
    else:
        placement_pt = wild_card_rank_pt[placement-1]
        kill_pt = kills
        rank_pt = placement_pt + kill_pt
    return rank_pt

# 1試合分のデータ取得
def make_team_score_1play(game, mode):
    team_score = {}
    players_info = game["matches"][0]["player_results"]

    for player_info in players_info:
        team_name = player_info["teamName"]
        kills = player_info["kills"]
        placement = player_info["teamPlacement"]
        total_pt = calc_rank_pt(placement, kills, mode)

        # チームリスト初期化処理
        if team_name not in team_score:
            team_score[team_name] = {
                "kills": kills,
                "placement": placement,
                "total_pt": total_pt
            }
    # トータルスコア、キル数順で並び替え
    sorted_score = dict(
        sorted(
            team_score.items(),
            key=lambda x: (x[1]["total_pt"], x[1]["kills"], -x[1]["placement"]),
            reverse=True
        )
    )
    return sorted_score

# メイン処理
def main(file_path, mode):
    # ゲーム情報取得
    game = game_load(file_path)

    
    score = make_team_score_1play(game, mode)

    # 表示処理
    for i, (team, v) in enumerate(score.items(), start=1):
            print(
                f"{i:>2} "
                f"{team:<18} "
                f"キル数:{v['kills']:>5} "
                f"順位:{v['placement']:>6} "
                f"トータルスコア{v['total_pt']:>6}"
            )

if __name__ == "__main__":
    # 読み取るjsonデータのファイルパスをここに
    file_path = "./games/normal_1.txt"
    # 通常試合ならTrue, ロイヤルカードならFalseを入れる
    mode = True

    main(file_path, mode)
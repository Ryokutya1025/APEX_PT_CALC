import json

# ファイルパス
file_path = "./games/normal_1.txt"
team_list = {}

# ゲームのロード
def game_load(file_path):
    # ファイルのロード
    with open(file_path, 'r', encoding='utf-8') as f:
        game = json.load(f)
    return game

game = game_load(file_path)

# ポイント集計 modeに通常試合ならtrue, ロイヤルカードならfalseを入れる
def calc_pt(placement, team_kill_count, mode):
    # 総ポイント数
    total_score = {}
    normal_rank_pt = [24,18,14,10,8,6,6,4,4,4,2,2,2,2,2,0,0,0,0,0]
    wild_card_rank_pt = [10,9.8,7,6,5,4,3,2,1]

# 1試合分のデータ取得
def make_team_list(game, mode):
    players_info = game["matches"][0]["player_results"]

    for player_info in players_info:
        team_name = player_info["teamName"]
        kills = player_info["kills"]
        placement = player_info["teamPlacement"]
        total_pt = calc_pt(placement, kills, mode)

        # チームリスト初期化処理
        if team_name not in team_list:
            team_list[team_name] = {
                "kills": 0,
                "placemeent": placement,
                "total_pt": 0
            }

    

make_team_list(game)

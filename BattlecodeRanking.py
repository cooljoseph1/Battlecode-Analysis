#On Battlecode Top Finalists
def optimize(s, wins, losses):    
    return s - (sum(a/(s+a) for a in losses) - sum(s/(s+a) for a in wins) + s-1)/(1 + sum(a/(s+a)**2 for a in wins) + sum(a/(s+a)**2 for a in losses))

import json
with open("pretty-rounds.txt") as f:
    data = f.read()
tournament = json.loads(data)
games = []
for r in tournament:
    games+=r["games"]
players = set()
for g in games:
    players.add(g["team 1"])
    players.add(g["team 2"])
player_games = dict()
player_matches = dict()
for p in players:
    player_games[p] = [g for g in games if g["team 1"] == p or g["team 2"] == p]
    player_matches[p] = []
    for game in player_games[p]:
        for match in game["matches"]:
            player_matches[p].append(match)
print("\n".join(str(k) for k in player_matches["Double J"]))
"""
################################################################################
#This makes the rounds into a pretty looking format.

with open("rounds.json") as f:
    game_dump = f.read()

import json
games = json.loads(game_dump)

new_games = []
for i, _round in enumerate(games):
    new_games.append(dict())
    new_games[i]["games"] = []
    team_list = _round["team_list"] if type(_round["team_list"][0][0]) is int else _round["team_list"][0]
    winners = _round["winners"] if type(_round["winners"][0][0]) is int else _round["winners"][0]
    for j in range(len(team_list)//2):
        game = dict()
        game["team 1"] = team_list[2*j][1] if team_list[2*j] is not None else None
        game["team 2"] = team_list[2*j+1][1] if team_list[2*j+1] is not None else None
        game["winner"] = winners[j][1]
        game["matches"] = []
        flip = 1
        for match in _round["matches"][j]:
            flip = 1-flip
            temp = dict()
            if(flip==0):
                temp["red"] = game["team 1"]
                temp["blue"] = game["team 2"]
            else:
                temp["red"] = game["team 2"]
                temp["blue"] = game["team 1"]
            if match[0] == "redwon":
                if flip==0:
                    temp["winner"] = game["team 1"]
                    temp["loser"] = game["team 2"]
                else:
                    temp["winner"] = game["team 2"]
                    temp["loser"] = game["team 1"]
            else:
                if flip==0:
                    temp["winner"] = game["team 2"]
                    temp["loser"] = game["team 1"]
                else:
                    temp["winner"] = game["team 1"]
                    temp["loser"] = game["team 2"]
            temp["url"] = match[1]
            game["matches"].append(temp)
        new_games[i]["games"].append(game)
        
with open("pretty-rounds.txt", 'w') as f:
    f.write(json.dumps(new_games, indent = 4))
"""

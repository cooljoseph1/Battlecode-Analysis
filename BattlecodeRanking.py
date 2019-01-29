#On Battlecode Top Finalists
class Player:
    def __init__(self, name):
        self.score = 0.5
        self.temp_score = self.score
        self.name = name
    def set_matches(self, matches):
        self.matches = matches
        self.wins = [val for val in self.matches if val["winner"] == self]
        self.losses = [val for val in self.matches if val["loser"] == self]
    def optimize(self):
        #self.temp_score = self.score + (sum((1-game["winner"].score)*(game["loser"].score) for game in self.wins) - sum((1-game["winner"].score)*(game["loser"].score) for game in self.losses))/len(self.matches)
        #print(self.temp_score - self.score)
        """if(self.name == "Standard Technology"):
            print("==================")
            print((sum((1-game["winner"].score)*game["loser"].score for game in self.wins)+0.5))
            print([((1-game["winner"].score), game["loser"].score, game["winner"].name, game["loser"].name) for game in self.wins])
            print((sum((1-game["winner"].score)*game["loser"].score for game in self.matches)+1))
            print([((1-game["winner"].score), game["loser"].score, game["winner"].name) for game in self.matches])
        """
        self.temp_score = (sum((1-game["winner"].score)*game["loser"].score for game in self.wins)+0.5)/(sum((1-game["winner"].score)*game["loser"].score for game in self.matches) + 1)
        #self.score = self.score - sum(g["loser"].score/(g["winner"].score + g["loser"].score) for g in self.matches)/(1 + sum(g["loser"].score/(self.score + g["loser"].score)**2 for g in self.wins) + sum(g["winner"].score/(self.score + g["winner"].score)**2 for g in self.wins))
        #self.score = abs(self.score)
    def finalize(self):
        self.score = self.temp_score
    def __str__(self):
        return "{0:40} {1}".format(str(self.name), str(self.score))
    
    
import json
with open("pretty-rounds.txt") as f:
    data = f.read()
tournament = json.loads(data)
games = []
for r in tournament:
    games+=r["games"]
player_names = set()
for g in games:
    player_names.add(g["team 1"])
    player_names.add(g["team 2"])
players = dict((name, Player(name)) for name in player_names)

player_games = dict()
player_matches = dict()
for p in players:
    player_games[p] = [g for g in games if g["team 1"] == p or g["team 2"] == p]
    player_matches[p] = []
    for game in player_games[p]:
        for match in game["matches"]:
            new_match = dict()
            new_match["winner"] = players[match["winner"]]
            new_match["loser"] = players[match["loser"]]
            
            player_matches[p].append(new_match)
            
for key,val in player_matches.items():
    players[key].set_matches(val)
    
for i in range(10000):
    for j in players.values():
        j.optimize()
        j.finalize()
        
s = list(players.values())
print("\n".join(str(x) for x in sorted(s, key = lambda p:p.score)))
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

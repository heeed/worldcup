import json
import urllib.request 
import operator 
with urllib.request.urlopen("https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json") as url: data = json.loads(url.read().decode())

def getTeamNumber(team_number):
  matches = [d for d in teams if d['id'] == team_number]
  return(matches[0]['name'])

def getStadiumName(stadium_number):
  matches = [d for d in stadiums if d['id'] == stadium_number]
  return(matches[0]['name'])


stadiums = data['stadiums']
teams = data['teams']
knockout = data['knockout']
groups = data['groups']
groups2 = sorted(groups.keys())

print("groups: "+str(type(groups)))
print("stadiums: "+str(type(stadiums)))
print("teams: "+str(type(teams)))
print("knockout: "+str(type(knockout)))
print(" ")
print("Sorted group keys: "+str(groups2))
print(groups.keys())
print(knockout.keys())
print(" ")

for x in groups['a']['matches']:


  print("Match: "+str(x['name']))
  print("Home Team: "+getTeamNumber(x['home_team']))
  print("Away Team: "+getTeamNumber(x['away_team']))
  print("Stadium: "+getStadiumName(x['stadium']))
  print("Date: "+str(x['date']))
  print(" ")


#World Cup Automator
#
#https://github.com/heeed/worldcup
#based on https://github.com/lsv/fifa-worldcup-2018
#
#This work is licensed under the terms of the MIT license.  
#For a copy, see <https://opensource.org/licenses/MIT>.
#
#Requires the arrow library 

import json,arrow
import urllib.request 
import operator 
with urllib.request.urlopen("https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json") as url: data = json.loads(url.read().decode())
#needed functions: getTeamName(team_number), getStadium(stadium number)

timeNow = arrow.utcnow()
dateNow = arrow.utcnow().date()
print(timeNow.date())

stadiums = data['stadiums']
teams = data['teams']
knockout = data['knockout']
groups = data['groups']
groupsSorted = sorted(groups.keys())

def getTeamName(team_number):
  matches = [d for d in teams if d['id'] == team_number]
  return(matches[0]['name'])

def getStadiumName(stadium_number):
  matches = [d for d in stadiums if d['id'] == stadium_number]
  return(matches[0]['name'])

def formatScores(homeTeamScore,awayTeamScore):
  if homeTeamScore > awayTeamScore:
    message = "and they won "+str(homeTeamScore)+":"+str(awayTeamScore)
  elif homeTeamScore < awayTeamScore:
    message = "and they lost "+str(homeTeamScore)+":"+str(awayTeamScore)
  else:
    message = "and it was a draw "+str(homeTeamScore)+":"+str(awayTeamScore)
  return message

def getAllMatchDetails(matchID,homeTeam,awayTeam,homeTeamScore,awayTeamScore,stadium,matchDate):
 message = ""
 homeTeam = getTeamName(homeTeam)
 awayTeam = getTeamName(awayTeam)
 stadium = getStadiumName(stadium)
 if matchDate > timeNow:
   message = str(homeTeam+ " will play "+awayTeam+" at the "+stadium+" on the "+matchDate.format('DD MMMM YYYY'))
 elif matchDate < timeNow:
   score = formatScores(homeTeamScore,awayTeamScore)
   message = str(homeTeam+ " played "+awayTeam+" at the "+stadium+" on the "+matchDate.format('DD MMMM YYYY')+" "+score)
 return message

def getTodaysMatchDetails(matchID,homeTeam,awayTeam,homeTeamScore,awayTeamScore,stadium,time):
 message = ""
 homeTeam = getTeamName(homeTeam)
 awayTeam = getTeamName(awayTeam)
 stadium = getStadiumName(stadium)
 if time > timeNow:
   message = str(homeTeam+ " will play "+awayTeam+" today at the "+stadium+" "+time.humanize())
 else:
   message = str(homeTeam+ " kicked off against "+awayTeam+" today at the "+stadium+" "+time.humanize())
 return message

def allGroupMatches():
  for group in groupsSorted:
    print("Group "+str(group)+" Matches:") 
    for fixture in range(len(groups[group]['matches'])):
    
      matchDate = arrow.get(groups[group]['matches'][fixture]['date'])
      print(getAllMatchDetails(groups[group]['matches'][fixture]['name'],groups[group]['matches'][fixture]['home_team'],groups[group]['matches'][fixture]['away_team'],groups[group]['matches'][fixture]['home_result'],groups[group]['matches'][fixture]['away_result'],groups[group]['matches'][fixture]['stadium'],matchDate))
  
    print("\n")

def todaysMatches():
 
  message = "Todays matches:\n"
  for group in groupsSorted:
    for fixture in range(len(groups[group]['matches'])):
      matchDate = arrow.get(groups[group]['matches'][fixture]['date']).date()
      matchTime = arrow.get(groups[group]['matches'][fixture]['date'])
      
      if matchDate == dateNow and groups[group]['matches'][fixture]['finished'] == False:
        message = message + getTodaysMatchDetails(groups[group]['matches'][fixture]['name'],groups[group]['matches'][fixture]['home_team'],groups[group]['matches'][fixture]['away_team'],groups[group]['matches'][fixture]['home_result'],groups[group]['matches'][fixture]['away_result'],groups[group]['matches'][fixture]['stadium'],matchTime)+"\n"
  return message

print(todaysMatches())

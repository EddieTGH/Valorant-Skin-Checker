from riotwatcher import LolWatcher
import discord

#currently can return rank, tier, and winrate for summoner name via discord command using this module below to interface with league API 
# https://riot-watcher.readthedocs.io/en/latest/riotwatcher/LeagueOfLegends/index.html
# https://www.youtube.com/watch?v=ml0lKDU5JvY could be helpful (using requests and json with league API raw to print out stats)

key="RGAPI-16bce2cc-2dd9-44b1-92a2-d4bddf46fa3b"
watcher = LolWatcher(key)


def printStats(summonerName):
    summoner = watcher.summoner.by_name("na1", summonerName)
    summonerID = summoner['id']
    stats=watcher.league.by_summoner("na1", summonerID)

    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']
    wins = int(stats[0]['wins'])
    losses = int(stats[0]['losses'])
    winrate= int(wins/(wins+losses)*100)
    #print(tier, rank, lp)
    #print("winrate: " + str(winrate)+"% ")
    #print(summonerName + " is currently ranked in " + str(tier), str(rank) + " with " + str(lp) + " LP and a " + str(winrate) + "% winrate.")
    userData = summonerName + " is currently ranked in " + str(tier) + ", " + str(rank) + " with " + str(lp) + " LP and a " + str(winrate) + "% winrate."
    return userData

#serData = printStats("EddieTGH12")
#print(userData)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$stats'):
        summonerName = message.content.split("$stats ",1)[1]
        #print("summonername: " + summonerName)
        userData = printStats(summonerName)
        await message.channel.send(userData)

client.run("ODgyOTkxNTMxOTY1OTQ3OTY0.YTDb8g.8nrYM2nYkK_uGnufbL4tvZaWpf8")
 
import discord
import random
import time
import threading 
from discord.utils import get
intents = discord.Intents().all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
global IfAuctionStarted
IfAuctionStarted = False
global StartTimer
StartTimer = False

@client.event
async def on_message(message):
    admin1 = message.author.guild.get_member(censored)
    admin2 = message.author.guild.get_member(censored)
    admin3 = message.author.guild.get_member(censored)
    if message.author == client.user:
        return
    if message.author == admin1 or message.author == admin2 or message.author == admin3:
      if message.content.startswith('$auction'):
        global channel
        channel = message.channel
        global IfAuctionStarted
        if IfAuctionStarted == False:
          print('You have started an auction')
          message1 = str(message.content).split(' ')
          IfAuctionStarted = True
          global StartTimer
          StartTimer = True
          global Winner
          Winner = 'N/A'
          global Item
          Item = message1[1]
          global StartingPrice
          StartingPrice = message1[2]
          global Seller
          Seller = message1[3]
          global CurrentPrice
          CurrentPrice = StartingPrice
          global TimeLimit
          TimeLimit = message1[4]
          global TimerAction
          def TimerAction():
              global timer
              global IfAuctionStarted
              IfAuctionStarted = ('A')
          timer = threading.Timer(int(TimeLimit),TimerAction)
          timer.start()
          await channel.send('An auction for ' + Item + ' has started with a selling price of ' + StartingPrice + ', with the seller: ' + Seller + ' for ' + TimeLimit + ' seconds')
        else:
          await channel.send('An auction has already started!')
      if message.author == admin1 or message.author == admin2 or message.author == admin3:  
        if message.content.startswith('$end'):
          if IfAuctionStarted == True:
            await channel.send('The auction has now ended.')
            await channel.send('The winner is ' + str(Winner) + ' with a bid of ' + str(CurrentPrice))
            IfAuctionStarted = False
    if message.content.startswith('$bid'):
       message1 = str(message.content).split(' ')
       Bid = message1[1]
       if IfAuctionStarted == True:
        if int(Bid) > int(CurrentPrice):
          Winner = str(message.author)
          await channel.send(Winner + ' now holds the highest bid on '+ str(Item) + ' with a bid of ' + str(Bid)) 
          CurrentPrice = Bid
        else:
          await channel.send('Please bid a higher amount!')
    if message.content.startswith('$results'):
      channel = message.channel
      if IfAuctionStarted == False:
        await channel.send('No Results Found!(Results are Wiped after Retrieving Once)')
      if IfAuctionStarted == True:
        await channel.send('An auction is still in session!')
      elif IfAuctionStarted == 'A':
        await channel.send('The auction has run out of time')
        await channel.send('The winner is ' + str(Winner) + ' with a bid of ' + str(CurrentPrice))
        IfAuctionStarted = False





client.run('censored')

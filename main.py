from keep_alive import keep_alive
import discord
import os
import requests
import json
import random
import time
from datetime import datetime
from replit import db

min = 1
max = 6
client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('I am logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if message.content.startswith('.bpin'):
    await message.delete()
    embed = discord.Embed(
      title=str("Kerala^Kings"),
      color=discord.Color.gold(),
      timestamp=datetime.utcnow()
    )
    embed.set_author(
      name=message.author.display_name,
      icon_url=message.author.avatar_url
    )
    embed.set_footer(
      text=client.user.name,
      icon_url=client.user.avatar_url
    )
    embed.add_field(
      name="test subject",
      value='this is a test :wink:',
      inline=False
    ) 
    await message.channel.send(embed=embed)
  #----hello command for everone----#

  if message.content.startswith('.hello'):
    await message.channel.send('Welcome to Kerala^Kings CODM Clan Discord Server :wink:')
  
  #-----print all command-----#

  if message.content.startswith('.help'):
    await message.channel.send('You can communicate with me by typing\n .hello\n .inspire\n .ping \n .name \n .member \n .roll \n .play') 

    #-----print random quotes-----#
    
  if message.content.startswith('.inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  #------simple guessing game----#
  
  if message.content.startswith('.play'):
    num = random.randint(1,10)
    count= 3
    for i in range (0, 4):
      if i<=2:
        await message.channel.send(f"Choose a number between 1-10\n you have {count} chances")
        guess = await client.wait_for("message")
        if int(guess.content) > num:
          await message.channel.send("Your guess is too high")
        elif int(guess.content) == num:
          await message.channel.send("You guessed the correct number!")
        elif int(guess.content) < num:
          await message.channel.send("Your gess is too low")
        count = count - 1
      else:
        await message.channel.send(f"You lost! The number was {num} your guess was {guess.content}")
        if i == 3:
          break

  #----ping the bot----#
    
  if message.content.startswith('.ping'):
    latency = client.latency
    pingembed = discord.Embed(
      title = str("Kerala^Kings"),
      color = discord.Color.gold(),
      timestamp = datetime.utcnow()
    )
    pingembed.set_author(
      name = message.author.display_name,
      icon_url=message.author.avatar_url
    )
    pingembed.set_footer(
      text=client.user.name,
      icon_url=client.user.avatar_url
    )
    pingembed.add_field(
      name="Latency",
      value=f"Pong! ``{round (latency*1000)}ms``",
      inline=False
    ) 
    await message.channel.send(embed=pingembed)

  #-----print boot name----#      
  
  if message.content.startswith('.name'):
    await message.channel.send('My name is Ghost :robot:') 

  if message.content.startswith('.member'):
    await message.channel.send('MELVIN3152#1085\nelectronymous#7750\nNeville#9182\nRhishabh(EP)#8300\nshaiju#1573')
  if message.content.startswith('.roll'):
    await message.channel.send('Rolling the dice...:game_die:')
    x = random.randint(min, max)
    time.sleep(2)
    await message.channel.send(x)   

keep_alive()
client.run(os.getenv("TOKEN"))
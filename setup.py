import discord
import os
import requests
import json
import random
from time import sleep
from datetime import datetime

TOKEN_GHOST = os.environ['TOKEN']
TOKEN_STATS = os.environ['TOKEN1']
client = discord.Client()
client1 = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('I am logged in as {0.user}'.format(client))
 
@client1.event
async def on_ready():
    print('I am logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if message.content.startswith('.bpin'):
    if message.author.guild_permissions.administrator:
      
      await message.delete()
      embed = discord.Embed(
        title=message.guild.name,
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
        name="Our BOT's...",
        value="Official bot <@&825930442627743755> ,Type `.help` for commands list.\nOur Play bot <@&861272759677091851> ,Type `pls help` for command list.\nOur rank bot for chatting <@&872883107005624341> ,Type `!help` for commands list",
        inline=True
      ) 
      await message.channel.send(embed=embed)
    else:
      await message.channel.send(":no_entry: You don't have the permissions to do that")
  #----hello command for everone----#

  if message.content.startswith('.hello'):
    await message.channel.send(f'Welcome to {message.guild.name} CODM Clan Discord Server :wink:')
  
  #-----print all command-----#

  if message.content.startswith('.help'):
    helpembed = discord.Embed(
      title = str("List of available commands"),
      color = discord.Color.gold(),
      timestamp = datetime.utcnow()
    )
    helpembed.set_author(
      name = message.author.display_name,
      icon_url=message.author.avatar_url
    )
    helpembed.set_footer(
      text=client.user.name,
      icon_url=client.user.avatar_url
    )
    helpembed.add_field(
      name="General",
      value="`.hello` -prints welcome message\n`.inspire` -show random quotes\n`.ping` -ping the bot\n`.name` -print the nameof bot\n`.roll` -roll the dice\n`.play` -play guess the number game",
      inline=True
    )
    helpembed.add_field(
      name="Admin",
      value="`.say` -say something using bot",
      inline=True
    ) 
    msg = await message.channel.send(embed=helpembed)
    #await message.channel.send('You can communicate with me by typing\n .hello\n .inspire\n .ping \n .name \n .member \n .roll \n .play') 

    #-----print random quotes-----#
    
  if message.content.startswith('.inspire'):
    quote = get_quote()
    embed = discord.Embed(
      title=message.guild.name,
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
      name=".",
      value=quote,
      inline=False
    ) 
    await message.channel.send(embed=embed)
    #await message.channel.send(quote)
  
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
          break
        elif int(guess.content) < num:
          await message.channel.send("Your gess is too low")
        count = count - 1
      else:
        await message.channel.send(f"You lost! The number was {num} your guess was {i}")
        if i == 3:
          break

  #----ping the bot----#
    
  if message.content.startswith('.ping'):
    latency = client.latency
    pingembed = discord.Embed(
      title = message.guild.name,
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
      value=f"Pong! `{round (latency*1000)}ms`",
      inline=True
    ) 
    await message.channel.send(embed=pingembed)

  #-----print boot name----#      
  
  if message.content.startswith('.name'):
    await message.channel.send('My name is Ghost :robot:') 

  #-----roll dice -----
  if message.content.startswith('.roll'):
    rollembed = discord.Embed(
      title = message.guild.name,
      color = discord.Color.gold(),
      timestamp = datetime.utcnow()
    )
    rollembed.set_author(
      name = message.author.display_name,
      icon_url=message.author.avatar_url
    )
    rollembed.set_footer(
      text=client.user.name,
      icon_url=client.user.avatar_url
    )
    rollembed.add_field(
      name="Dice roll",
      value="Rolling the dice...:game_die:",
      inline=False
    ) 
    msg = await message.channel.send(embed=rollembed)
    x = random.randint(1, 6)
    time.sleep(2)
    if x==1:
     (y)=":one:"
    elif x==2:
      (y)=":two:"
    elif x==3:
      (y)=":three:"
    elif x==4:
     (y)=":four:"
    elif x==5:
      (y)=":five:"
    else:
      (y)=":six:"
      
    embed = discord.Embed(
      title=message.guild.name,
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
      name="Dice roll results",
      value=f"{y}",
      inline=True
    )
    await msg.edit(embed=embed)
  #say somthing using bot
  if message.content.startswith('.say'):
    command = message.content.strip(".say").split(" ")
    if message.author.guild_permissions.administrator:
      await message.delete()
      text = str(" ".join(command))
      sayembed = discord.Embed(
        title = message.guild.name,
        color = discord.Color.gold(),
        timestamp = datetime.utcnow()
      )
      sayembed.set_author(
        name = message.author.display_name,
        icon_url=message.author.avatar_url
      )
      sayembed.set_footer(
        text=client.user.name,
        icon_url=client.user.avatar_url
      )
      sayembed.add_field(
        name="Bot says...",
        value=text,
        inline=False
      ) 
      await message.channel.send(embed=sayembed)
    else:
      await message.delete()
      await message.channel.send(
                    ":no_entry: You dont't have the permission to do that!")
      await message.delete()

     
  if message.content.startswith('Pls rob'):
    await message.channel.send('This command is disabled fools')

@client1.event
async def on_message(msg):
    args = msg.content.split(" ")
    cmd = args[0]
    Channel = client.get_channel(919272383213367337)
    if msg.author == client.user:
        return
    if cmd == "!clear":
        await msg.channel.send(f'Clearing {args[1]} messages..')
        sleep(2)
        await msg.channel.purge(limit=int(args[1]))
    if cmd == "!ip":
        await msg.delete()
        sleep(2)
        embed = discord.Embed(
            title=msg.guild.name,
            color=discord.Color.gold(),
            timestamp=datetime.utcnow()
        )
        embed.set_footer(
            text=client.user.name,
            icon_url=client.user.avatar_url
        )

        embed.add_field(
            name='**@everyone**',
            value="Creating new ngrok tunnel and requesting for  IP pls wait....",
            inline=True
        )
        await Channel.send(embed=embed)
        await Channel.send("@everyone")
        res = r.get(url)
        await Channel.send("```" + res.text + "```")

    if "Server has started" in  msg.content:
        embed = discord.Embed(
            title=msg.guild.name,
            color=discord.Color.gold(),
            timestamp=datetime.utcnow()
        )
        embed.set_footer(
            text=client.user.name,
            icon_url=client.user.avatar_url
        )

        embed.add_field(
            name='**@everyone**',
            value="Creating new ngrok tunnel and requesting for  IP pls wait....",
            inline=True
        )
        await Channel.send(embed=embed)
        await Channel.send("@everyone")
        res = requests.get(url)
        await Channel.send("```" + res.text + "```")
    if "Server has stopped" in msg.content:
        await Channel.send("Destroying Tunnel...")
        await Channel.purge(limit=10)

client.run(TOKEN_GHOST)
client1.run(TOKEN_STATS)

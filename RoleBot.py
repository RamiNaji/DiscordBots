import discord
from discord.utils import get
from discord.ext import tasks
intents = discord.Intents().all()
client = discord.Client(intents=intents)

embed = discord.Embed(title="Role Manager", description="React with a certain color to gain a role", colour=0x000FF)
embed.set_author(name="censored")
embed.add_field(name="censored", value="React with 🟪 for censored, 🟧 for censored, and ⬛ for censored", inline=False)
embed.add_field(name="censored", value="React with 🟦 for censored,🟥 for censored,🟩 for censored, and 🟨 for censored", inline=True)


embed2 = discord.Embed(title="🔒 Channel Locked", colour=0xFF3131)

embed3 = discord.Embed(title="🔓 Channel Unlocked", colour=0x2ECC71)
embed4 = discord.Embed(title="To confirm, please react with the checkmark", colour=0xFF6700)

embed5 = discord.Embed(title="🔒 This server has gone into raid protection mode; please stand-by while we locate and resolve the problem", colour=0xFF3131)

embed6 = discord.Embed(title="⚠️ Trying to locate any rogue admins", colour=0xFF3131)

embed7 = discord.Embed(title="⚠️ All members with the adminstrator role have lost their role", colour=0xFF3131)

embed8 = discord.Embed(title="⚠️ No further damage can be done from the adminstrator side", colour=0xFF3131)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(censored'):
      if message.author.id == censored or message.author.id == censored or message.author.id ==censored or message.author.id == censored:
        channels3 = message.guild.channels
        role = get(message.guild.roles, name='V');
        for channel2 in channels3:
            if isinstance(channel2, discord.TextChannel): 
              await channel2.set_permissions(role, view_channel=False)
        ga = client.get_channelcensored)
        await ga.set_permissions(role, view_channel = True)
        await ga.send(embed=embed5)
        modchannel = client.get_channel(censored)
        await modchannel.send(embed=embed6)
        role10 = get(message.guild.roles,name='o')
        role11 = get(message.guild.roles,name='i')
        role12 = get(message.guild.roles,name='w')
        for member in role10.members:
          await member.remove_roles(role10)
        for member in role11.members:
          await member.remove_roles(role11)
        for member in role12.members:
          await member.remove_roles(role12)
        await modchannel.send(embed=embed6)
        await modchannel.send(embed=embed7)

    


    if message.content.startswith('censored'):
      if str(message.author.id) == 'censored':
          global channel
          channel = message.channel
          await message.delete()
          global embedmessage
          embedmessage = await message.channel.send(embed=embed)
          await embedmessage.add_reaction('🟪')
          await embedmessage.add_reaction('🟧')
          await embedmessage.add_reaction('⬛')
          await embedmessage.add_reaction('🟦')
          await embedmessage.add_reaction('🟥')
          await embedmessage.add_reaction('🟩')
          await embedmessage.add_reaction('🟨')
    if message.content.startswith('$lock'):
      if message.author.id == censored or message.author.id == censored or message.author.id == censored or message.author.id == censored:
        channels3 = message.guild.channels
        embed4message = await message.channel.send(embed=embed4)
        await embed4message.add_reaction('✅')
        global messagecheckid
        messagecheckid = embed4message.id
    if message.content.startswith('$unlock'):
      if message.author.id == censored or message.author.id == censored or message.author.id == censored or message.author.id == censored:
        channels3 = message.guild.channels
        role = get(message.guild.roles, name='V');
        for channel2 in channels3:
          if isinstance(channel2, discord.TextChannel): 
            await channel2.set_permissions(role, send_messages=True)
            await channel2.send(embed=embed3)

@client.event
async def on_reaction_add(reaction,user):
  if user == client.user:
    return
  if user.id == censored or user.id == censored or user.id == censored or user.id == censored:
    if str(reaction.message.id) == str(messagecheckid):
            if str(reaction) == '✅':
              role = get(reaction.message.guild.roles, name='v');
              channels3 = reaction.message.guild.channels
              for channel2 in channels3:
                if isinstance(channel2, discord.TextChannel): 
                  await channel2.set_permissions(role, send_messages=False)
                  await channel2.send(embed=embed2)
        


@client.event
async def on_raw_reaction_add(payload):
  Channel = censored
  guild = client.get_channel(Channel).guild
  user = get(guild.members, id= payload.user_id)
  reaction1 = payload.emoji.name
  reaction = str(reaction1)
  channel = client.get_channel(Channel)
  if str(channel.id) == str(Channel):
    Role1 = get(guild.roles, name="g")
    Role2 = get(guild.roles, name="f")
    Role3 = get(guild.roles, name="e")
    Role4 = get(guild.roles, name="z")
    Role5 = get(guild.roles, name="c")
    Role6 = get(guild.roles, name="a")
    Role7 = get(guild.roles, name="b")
    if str(reaction) == "🟧":
      if Role2 in user.roles:
        await user.remove_roles(Role2)
      if Role3 in user.roles:
        await user.remove_roles(Role3)
      if Role1 not in user.roles:
        await user.add_roles(Role1)


    if str(reaction) == "🟪":
      if Role1 in user.roles:
        await user.remove_roles(Role1)
      if Role3 in user.roles:
        await user.remove_roles(Role3)
      if Role2 not in user.roles:
        await user.add_roles(Role2)



    if str(reaction) == "⬛":
      if Role1 in user.roles:
        await user.remove_roles(Role1)
      if Role2 in user.roles:
        await user.remove_roles(Role2)
      if Role3 not in user.roles:
        await user.add_roles(Role3)


    if str(reaction) == "🟨":
      if Role5 in user.roles:
        await user.remove_roles(Role5)
      if Role6 in user.roles:
        await user.remove_roles(Role6)
      if Role7 in user.roles:
        await user.remove_roles(Role7)
      if Role4 not in user.roles:
        await user.add_roles(Role4)


    if str(reaction) == "🟥":
      if Role4 in user.roles:
        await user.remove_roles(Role4)
      if Role6 in user.roles:
        await user.remove_roles(Role6)
      if Role7 in user.roles:
        await user.remove_roles(Role7)
      if Role5 not in user.roles:
        await user.add_roles(Role5)



    if str(reaction) == "🟦":
      if Role4 in user.roles:
        await user.remove_roles(Role4)
      if Role5 in user.roles:
        await user.remove_roles(Role5)
      if Role7 in user.roles:
        await user.remove_roles(Role7)
      if Role6 not in user.roles:
        await user.add_roles(Role6)



    if str(reaction) == "🟩":
      if Role4 in user.roles:
        await user.remove_roles(Role4)
      if Role5 in user.roles:
        await user.remove_roles(Role5)
      if Role6 in user.roles:
        await user.remove_roles(Role6)
      if Role7 not in user.roles:
        await user.add_roles(Role7)



     




client.run('censored')

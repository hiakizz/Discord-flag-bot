import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='!')

countries = [
  ['Brazil', 'Canada', 'Japan', 'Spain', 'UnitedStates'],
  [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/275px-Flag_of_Brazil.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/305px-Flag_of_Canada_%28Pantone%29.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/290px-Flag_of_Japan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/255px-Flag_of_Spain.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/290px-Flag_of_the_United_States.svg.png',
  ]
]

sort = 0


def randomize():
  global control
  if sort == 0:
    control = random.randint(0, 4)
  return control


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == countries[0][randomize()]:
    await message.add_reaction('✅')

  global sort
  sort = 0

  await client.process_commands(message)


@client.command(name='p')
async def play(ctx):
  randomize()
  global sort
  sort = 1
  embed = discord.Embed(title='What is this flag name?', color=0x18191C)
  embed.set_image(url=countries[1][control])
  await ctx.send(embed=embed)


@client.command(name='htp')
async def howToPlay(ctx):
  await ctx.send(
    'How to play?\nType the command \'!p\', after that the overview of the game will appear, then type the name of the country that appears. If you get the answer right the bot will react with ✅.\n\(the names of the countries existing in the bot are located in the command \'!fl\'\)'
  )


@client.command(name='fl')
async def helpCommand(ctx):
  await ctx.send(
    'Currently existing flags are:\n•Brazil\n•Canada\n•Japan\n•Spain\n•UnitedStates'
  )


client.run(
  'YOUR BOT TOKEN')
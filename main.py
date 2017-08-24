# imports discord library and the commands
import discord
from discord.ext import commands
from random import randint

# Liberty Prime Quotes
quotes = ['Chairman Cheng will fail: China will fall!', 'Communist threat assessment: Minimal. Scanning defenses...', 'Satellite Uplink detected. Analysis of Communist transmission pending.', 'Warning! Warning! Red Chinese Orbital Strike Imminent! All personnel should reach minimum safe distance immediately!', 'Repeat: Red Chinese orbital strike inbound! All U.S. Army personnel must vacate the area immediately! Protection protocols engaged!', 'Democracy is the essence of good. Communism, the very definition of evil.']

# Defines Bot, Bot prefix, and bot description
bot = commands.Bot(command_prefix = 'test!', description = 'Hopefully this works!')

# Bot event notifies users when it logs on
@bot.event
async def on_ready():
	print('Liberty Prime is online. All systems nominal. Weapons hot. Mission: the destruction of any and all Chinese communists')

@bot.command()
async def hello():
	await bot.say("Hello!")

@bot.command()
async def prime():
	listLength = len(quotes) 
	randomInteger = randint(0, listLength)
	await bot.say(quotes[randomInteger])

bot.run('MzUwMTI2MzEwMDk1MzIzMTM4.DH_h_g.jxUX0josU7SPHqBCZwb4N-yGSf8')


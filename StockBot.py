import discord
import logging
from dotenv import load_dotenv
import os 


def main():
	# configure tokens
	tokens = set_tokens()

	# configure logging
	set_logging()

	intents = discord.Intents.default()
	intents.messages = True

	bot = StockBot(intents=intents)
	bot.run(tokens[0])

def set_tokens():
	# loads dotenv files in the local directory
	load_dotenv()
	TOKEN = os.getenv('DISCORD_TOKEN')
	GUILD = os.getenv('DISCORD_GUILD')
	return [TOKEN, GUILD]

def set_logging():
	logger = logging.getLogger('discord')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)



class StockBot(discord.Client):
	async def on_ready(self):
		print(f"We've logged on as {self.user}.")
		# doesn't need to be awaited - non blocking function

	async def on_message(self, message):
		if message.author == self.user:
			return
		if message.content.startswith('$hello'):
			await message.channel.send('hello!')
	
	async def help_call(self, message):
		if message.content("help"):
			await message.channel.send('let me give you some help')